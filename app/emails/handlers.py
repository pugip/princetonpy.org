from django.dispatch import receiver
from django_ses.signals import bounce_received, complaint_received

from emails.models import EmailFailure


@receiver(bounce_received)
def bounce_handler(sender, mail_obj, bounce_obj, raw_message, *args, **kwargs):
    # message_id = mail_obj["messageId"]
    # recipient_list = mail_obj["destination"]
    failure = EmailFailure(
        raw_message=raw_message,
        failure_type=EmailFailure.BOUNCE
    )
    failure.save()


@receiver(complaint_received)
def complaint_handler(sender, mail_obj, complaint_obj, raw_message, *args, **kwargs):
    # message_id = mail_obj["messageId"]
    # recipient_list = mail_obj["destination"]
    failure = EmailFailure(
        raw_message=raw_message,
        failure_type=EmailFailure.COMPLAINT
    )
    failure.save()
