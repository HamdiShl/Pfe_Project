from django.db import models

# Create your models here.

# models.py
from django.db import models

class TemperatureData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()

class HumidityData(models.Model):
    timestamp = models.DateTimeField()
    humidity = models.FloatField()

class LightData(models.Model):
    timestamp = models.DateTimeField()
    light = models.FloatField()



class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"SensorData ({self.timestamp})"


class Battery(models.Model):
    maxVotage=models.FloatField(max_length=100,null=True)
    minVoltage=models.FloatField(max_length=100,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return str(self.maxVotage)+"%"




