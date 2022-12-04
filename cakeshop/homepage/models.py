
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.

class SignFranchise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand=models.CharField(max_length=30,default="None")
    address=models.CharField(max_length=50,default="None")
    pin=models.CharField(max_length=30, default="None")
    gst=models.CharField(max_length=15,default="None")
    name=models.CharField(max_length=30,default="None")
    mobile=models.CharField(max_length=10,default="None")

class Signhome(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=50,default="None")
    pin=models.CharField(max_length=30, default="None")
    fss=models.ImageField(null=True,blank=True,upload_to='images/')
    name=models.CharField(max_length=30,default="None")
    mobile=models.CharField(max_length=10,default="None")

class Cakeitem(models.Model):
    user=ForeignKey(User, on_delete=models.CASCADE)
    brand=models.CharField(max_length=20,default="None")
    name=models.CharField(max_length=30, default="None")
    category=models.CharField(max_length=10)
    cimg=models.ImageField(null=True,blank=True,upload_to='images/')
    price500=models.IntegerField(null=True,blank=True)
    price1=models.IntegerField(null=True,blank=True,default=None)
    price2=models.IntegerField(null=True,blank=True,default=None)
    price3=models.IntegerField(null=True,blank=True,default=None)
    des=models.CharField(max_length=100,default="None")

class SignCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=150,default="None")
    pin=models.CharField(max_length=30, default="None")
    name=models.CharField(max_length=30,default="None")
    mobile=models.CharField(max_length=10,default="None")
    yearlsub=models.CharField(max_length=10,default="None")
  