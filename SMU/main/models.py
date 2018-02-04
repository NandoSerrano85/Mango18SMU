from django.db import models
from django_google_maps import fields as map_fields


class User(models.Model):
    EIN = models.CharField(max_length=9)
    email = models.EmailField(primary_key=True)
    business_name = models.CharField(max_length=300)
    principal = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    organization_type = models.CharField(max_length=30)
    business_type = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'


class SmallBusiness(models.Model):
    rank = models.DecimalField(max_digits=8, decimal_places=3)
    ratio_ta = models.DecimalField(max_digits=8, decimal_places=3)
    ratio_tbl = models.DecimalField(max_digits=8, decimal_places=3)
    amount = models.IntegerField()
    number = models.IntegerField()

    class Meta:
        db_table = 'smallbusiness'
        unique_together = (('rank', 'amount', 'number', 'ratio_ta', 'ratio_tbl'),)

class MicroBusiness(models.Model):
    rank = models.DecimalField(max_digits=8, decimal_places=3)
    amount = models.IntegerField()
    number = models.IntegerField()

    class Meta:
        db_table = 'microbusiness'
        unique_together = (('rank', 'amount', 'number', ),)

class Financial(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=15)
    small_business = models.ForeignKey(SmallBusiness, on_delete=models.CASCADE)
    micro_business = models.ForeignKey(MicroBusiness, on_delete=models.CASCADE)
    size = models.CharField(max_length=2)
    cc_amount = models.CharField(max_length=30)
    asset_size = models.CharField(max_length=30)

    class Meta:
        db_table = 'financial'

class Legislation(models.Model):
    city = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=5)
    legCode = models.TextField(primary_key=True, max_length=100)
    summary = models.TextField(max_length=300)

    class Meta:
        db_table = 'legislation'
