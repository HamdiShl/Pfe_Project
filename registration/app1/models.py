from django.db import models

# Create your models here.


class Capteurs(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    courant = models.DecimalField(max_digits=5, decimal_places=2)
    luminosite = models.DecimalField(max_digits=5, decimal_places=2)
    date_mesure = models.DateTimeField(auto_now_add=True)

class Actionneur(models.Model):
    regulateur_charge = models.CharField(max_length=100)
    date_mesure = models.DateTimeField(auto_now_add=True)


