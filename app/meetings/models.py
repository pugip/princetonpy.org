from django.db import models
from newsletter.models import Message
from tinymce.models import HTMLField


class Meeting(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=140)
    short_description = HTMLField()
    meeting_text = HTMLField()
    announcement = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)

    @property
    def date_slug(self) -> str:
        return self.date.date().isoformat()

    @property
    def date_str(self) -> date:
        return self.date.date()
