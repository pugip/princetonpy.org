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
    save_path = subscribers_folder / f"{formatted_date}.csv"
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "w") as f:
        csv_file = csv.writer(f, delimiter=",")
        for subscriber in subscriptions:
            if not subscriber.subscribed:
                continue
            email = subscriber.get_email()
            name = subscriber.get_name()
            newsletter_title = subscriber.newsletter.title
            if subscriber.subscribe_date:
                subscribe_date = subscriber.subscribe_date.date()
            else:
                subscribe_date = None
            csv_file.writerow([name, email, newsletter_title, subscribe_date])
