# Generated by Django 3.2.6 on 2021-10-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meeting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField()),
                ("title", models.CharField(max_length=140)),
                ("meeting_text", models.TextField()),
                ("announcement_link", models.URLField()),
            ],
        ),
    ]
