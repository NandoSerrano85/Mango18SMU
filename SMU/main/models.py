from django.db import models
from django_google_maps import fields as map_fields


class User(models.Model):
    EIN = models.CharField(primary_key=True, max_length=9)
    email = models.EmailField()
    business_name = models.CharField(max_length=300)
    principal = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    organization_type = models.CharField(max_length=30)
    business_type = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)


# Create your models here.

class Map(models.Model):
    class Meta:
        unique_together = (('zipcode', 'street'),)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(primary_key=True, max_length=5)
    street = models.CharField(max_length=10)
    county = models.CharField(max_length=25)
    latitude = models.CharField(max_length=2)
    longitude = models.CharField(max_length=2)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

class Legislation(models.Model):
    maps = models.ForeignKey(Map, on_delete=models.CASCADE)
    legCode = models.TextField(primary_key=True, max_length=100)
