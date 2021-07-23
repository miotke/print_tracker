# Generated by Django 3.2.5 on 2021-07-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrintTracker',
            fields=[
                ('print_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('total_print_time', models.TimeField()),
                ('date_of_print', models.TimeField()),
                ('material_used', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=100)),
                ('stl_file', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
