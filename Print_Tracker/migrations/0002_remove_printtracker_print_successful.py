# Generated by Django 3.2.5 on 2021-07-28 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("print_tracker", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="printtracker",
            name="print_successful",
        ),
    ]
