from django.db import models
from django.utils import timezone


# Create your models here.
class PrintTracker(models.Model):

    today = timezone.now

    print_name = models.CharField(max_length=100, primary_key=True)
    total_hours_printed = models.IntegerField(default=0)
    total_minutes_printed = models.IntegerField(default=0)
    date_of_print = models.DateField(default=today)
    material_used = models.CharField(max_length=25, blank=True)
    color = models.CharField(max_length=100, blank=True)
    gcode_file = models.FileField(blank=True)


    def save(self):
        super().save()

    
    def __str__(self):
        return self.print_name
