# Generated by Django 3.2.6 on 2021-10-22 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0005_auto_20190918_0122"),
        ("meetings", "0003_auto_20211020_0035"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="announcement",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="newsletter.message",
            ),
        ),
    ]
