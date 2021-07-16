from django.db import models
from homepage.validators import OptionalSchemeURLValidator


class MeetingLink(models.Model):
    link = models.CharField(max_length=300, blank=True, null=True, validators=[OptionalSchemeURLValidator])
    link_text = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        if len(self.link) > 10:
            return f"{self.link[:10]}...: {self.link_text or 'no text supplied'}"
        return f"{self.link}: {self.link_text or 'no text supplied'}"
