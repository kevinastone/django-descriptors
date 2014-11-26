import urlparse
from django.db import models


class OriginalBookmark(models.Model):
    url = models.URLField()

    @property
    def hostname(self):
        return urlparse.urlparse(self.url).hostname


class URLFieldProxy(unicode):
    @property
    def hostname(self):
        return urlparse.urlparse(self).hostname


class ProxyFieldDescriptor(object):
    def __init__(self, field_name, proxy_class=None):
        self.field_name = field_name
        self.proxy_class = proxy_class

    def __get__(self, instance=None, owner=None):
        # grab the original value before we proxy
        value = instance.__dict__[self.field_name]
        if value is None:
            # We can't proxy a None through a unicode sub-class
            return value
        return self.proxy_class(value)

    def __set__(self, instance, value):
        instance.__dict__[self.field_name] = value


class SomeObject(object):
    wormhole = ProxyFieldDescriptor('url', URLFieldProxy)

    def __init__(self, url):
        self.url = url


class HostnamedURLField(models.URLField):
    def contribute_to_class(self, cls, name):
        super(HostnamedURLField, self).contribute_to_class(cls, name)
        # Add our descriptor to this field in place of of the normal attribute
        setattr(cls, self.name, ProxyFieldDescriptor(self.name, URLFieldProxy))


class Bookmark(models.Model):
    url = HostnamedURLField()
