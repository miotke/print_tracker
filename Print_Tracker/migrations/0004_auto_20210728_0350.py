# Generated by Django 3.2.5 on 2021-07-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print_tracker', '0003_auto_20210728_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printtracker',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='printtracker',
            name='material_used',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]