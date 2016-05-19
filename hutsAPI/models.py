from django.db import models

# Create your models here.

#Class to model buildings, one building can have different Huts
#on it
class Building (models.Model):
    zip = models.IntegerField(null=True)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null=True)
    street = models.CharField(max_length=100, null=True, blank = True)
    number = models.CharField(max_length=100, null=True, blank = True)
    bloc = models.CharField(max_length=10, blank=True)

    def __repr__(self):
      return 'Building: ' + str(self.street)+ ' ' + str(self.number)

    def __unicode__(self):
        return self.code

#class to model Huts
class Hut(models.Model):
    code = models.CharField(max_length=30)
    DC = models.IntegerField()
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    telefon = models.IntegerField(null=True)
    flat = models.CharField(max_length=10, null=True)
    door = models.CharField(max_length=10, null=True)
    building = models.ForeignKey(Building,related_name='hut', default=0)

    def __unicode__(self):
        return self.code



