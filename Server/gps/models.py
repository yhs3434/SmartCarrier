from django.db import models
from django.utils import timezone

# Create your models here.

class Gps(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
    upload_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.name

    def __position__(self):
        return str(self.latitude)+", "+str(self.longitude)

class Beacon(models.Model):
    beacon = models.CharField(max_length=20)
    distance = models.FloatField(null=True)