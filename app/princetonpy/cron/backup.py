import csv
from pathlib import Path

from django.utils.datetime_safe import datetime
from newsletter.models import Subscription

from princetonpy.settings import BACKUP_PATH


def save_users():
    if BACKUP_PATH is None:
        return
    subscriptions = Subscription.objects.all()
    date = datetime.now().date()
    formatted_date = date.isoformat()
    subscribers_folder = Path(BACKUP_PATH) / "subscribers"
    save_path = subscribers_folder / formatted_date
    with open(save_path, "w") as f:
        csv_file = csv.writer(f, delimiter=",")
        for subscriber in subscriptions:
            email = subscriber.get_email
            name = subscriber.get_name
            csv_file.writerow([name, email])
