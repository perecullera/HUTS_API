from django.db import models

# Create your models here.

class Hut(models.Model):
    code = models.CharField(max_length=30)
    DC = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

class Address(models.Model):
    hut = models.ForeignKey(Hut)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    flat = models.IntegerField()
    door = models.IntegerField()
    postal_code = models.IntegerField()
    latitude = models.FloatField(blank = True)
    longitude = models.FloatField(blank=True)