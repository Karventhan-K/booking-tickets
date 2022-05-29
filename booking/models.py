from django.db import models


# Create your models here.
class ticket_booking(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    father_name = models.CharField(max_length=65)
    Gender = models.CharField(max_length=65)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=25)
    start_station = models.CharField(max_length=65)
    end_station = models.CharField(max_length=65)
