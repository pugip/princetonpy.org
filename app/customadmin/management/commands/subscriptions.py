import csv
from pathlib import Path

from django.core.management import BaseCommand
from newsletter.models import Subscription, Newsletter


def file_path(value: str) -> Path:
    path = Path(value)
    if path.is_file():
        return path
    else:
        raise FileNotFoundError(value)


class Command(BaseCommand):
    help = "Used for importing subscriptions."

    def add_arguments(self, parser):
        parser.add_argument("action", choices=["export", "import"])
        parser.add_argument("file", type=file_path)

    def handle(self, *args, **options):
        action = options["action"]
        file = options["file"]
        if action == "export":
            pass
            # subscriptions = Subscription.objects.all()
            # with open():
            #     for user in subscriptions:
            #         pass
        elif action == "import":
            with open(file, "r") as f:
                csv_file = csv.reader(f, delimiter=",")
                for row in csv_file:
                    name, email, title, subscribe_date = row
                    newsletter = Newsletter.objects.get(title=title)
                    Subscription.objects.create(
                        name=name,
                        email=email,
                        newsletter=newsletter,
                        subscribed=True,
                    )
