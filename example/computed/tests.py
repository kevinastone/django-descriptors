from .models import ProxyFieldDescriptor, URLFieldProxy


class SomeObject(object):
    # Let's add our descriptor on the `url` field substituting `URLFieldProxy`
    wormhole = ProxyFieldDescriptor('url', URLFieldProxy)

    def __init__(self, url):
        self.url = url


obj = SomeObject('http://example.com/asdf')

# Normal attribute access still works
obj.url

# Does obj.url have a hostname property?
try:
    obj.url.hostname
except AttributeError:
    pass

# What about accessing our descriptor field?
obj.wormhole

# Let's access the descriptor's property
obj.wormhole.hostname

# As you can see, the descriptor returns our proxy
type(obj.wormhole)

# But the proxy still *acts* like our original url attribute
obj.wormhole == obj.url
