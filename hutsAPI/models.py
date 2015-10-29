from django.db import models

# Create your models here.

class Hut(models.Model):
    code = models.CharField(max_length=30)
    DC = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telefon = models.IntegerField(null=True)
    street = models.CharField(max_length=100, null=True, blank = True)
    number = models.CharField(max_length=10, null=True, blank = True)
    flat = models.IntegerField(null=True)
    door = models.IntegerField(null=True)
    postal_code = models.IntegerField(null=True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null=True)

    def __unicode__(self):
        return self.code
