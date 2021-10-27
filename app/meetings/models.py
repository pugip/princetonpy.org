import datetime
from typing import Optional

from django.db import models
from newsletter.models import Message
from tinymce.models import HTMLField


class Meeting(models.Model):
    date = models.DateTimeField(null=True)
    title = models.CharField(max_length=140)
    short_description = HTMLField(default="")
    meeting_text = HTMLField(default="")
    no_announcement = models.BooleanField(default=False)
    announcement = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)

    @property
    def date_slug(self) -> Optional[str]:
        try:
            return self.date.date().isoformat()
        except AttributeError:
            pass

    @property
    def date_str(self) -> Optional[datetime.date]:
        try:
            return self.date.date()
        except AttributeError:
            pass
