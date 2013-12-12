from django.db import models


class BaseEvent(models.Model):
    """
    Base fields for a Mandrill email event.
    """
    name = models.CharField(max_length=100, help_text=u'Event type name.')
    payload = models.TextField(help_text=u'JSON-encoded event data.')
    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text=(u'Time the event was received. Note this may differ from'
                   ' the "ts" key in the Mandrill payload, which records the'
                   ' time the event ocurred.')
    )

    class Meta:
        app_label = 'djrill'
        abstract = True


class Event(BaseEvent):
    """
    Concrete implementation of an Event that is installed by the app.
    """
    class Meta:
        app_label = 'djrill'
