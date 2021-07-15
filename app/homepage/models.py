from django.db import models
from homepage.validators import OptionalSchemeURLValidator


class MeetingLink(models.Model):
    link = models.CharField(max_length=300, blank=True, null=True, validators=[OptionalSchemeURLValidator])
    link_text = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.link}: {self.link_text or 'no text supplied'}"
