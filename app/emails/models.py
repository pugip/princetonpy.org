from django.db import models


class EmailFailure(models.Model):
    BOUNCE = "BO"
    COMPLAINT = "CO"
    FAILURE_CHOICES = [
        (BOUNCE, "Bounce"),
        (COMPLAINT, "Complaint"),
    ]

    raw_message = models.TextField()
    failure_type = models.CharField(
        max_length=2,
        choices=FAILURE_CHOICES,
        default=BOUNCE,
    )

    def __str__(self):
        return f"{self.failure_type}"
