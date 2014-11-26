from django.utils import timezone

from .models import TimestampedBooleanDescriptor


class SomeObject(object):
    # Let's add our descriptor on the `timestamp` field
    boolean = TimestampedBooleanDescriptor('timestamp')

    def __init__(self, timestamp=None):
        self.timestamp = timestamp


obj = SomeObject()
obj.timestamp
obj.boolean

obj.timestamp = timezone.now()
obj.boolean

obj.boolean = False
obj.timestamp
obj.boolean = True
obj.timestamp
