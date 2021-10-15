from typing import Optional

from django.template.defaultfilters import date
from newsletter.models import Newsletter, Message, Submission


def get_announcement_text(submission: Submission) -> str:

    return
