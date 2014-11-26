from django.db import models
from django.utils import timezone


class OriginalBlogPost(models.Model):
    content = models.TextField()
    published_at = models.DateTimeField(null=True, default=None)


class TimestampedBooleanDescriptor(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance=None, owner=None):
        return instance.__dict__[self.name] is not None

    def __set__(self, instance, value):
        value = bool(value)
        if value != self.__get__(instance):
            if value:
                instance.__dict__[self.name] = timezone.now()
            else:
                instance.__dict__[self.name] = None


class TimestampedBooleanField(models.DateTimeField):
    """
    A Boolean field that also captures the timestamp when the value was set.

    This field stores a timestamp in the database when set.  It can be accessed
    as a boolean using the property argument (when not provided, it defaults to
    is_{field_name}).
    """
    def __init__(self, *args, **kwargs):
        self.property_name = kwargs.pop('property', None)
        kwargs['null'] = True
        super(TimestampedBooleanField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(TimestampedBooleanField, self).contribute_to_class(cls, name)
        # Use the defined boolean property name or pick a default
        property_name = self.property_name or 'is_{0}'.format(name)
        setattr(cls, property_name, TimestampedBooleanDescriptor(self.name))


class BlogPost(models.Model):
    content = models.TextField()
    published_at = TimestampedBooleanField(property='is_published')
