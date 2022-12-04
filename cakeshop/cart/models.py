from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from homepage.models import Cakeitem
from django.contrib.auth.models import User
# Create your models here.

#not used
class Cartitem(models.Model): 
    cid=models.ForeignKey(Cakeitem,on_delete=models.CASCADE)
    kg=models.IntegerField(default=1)
    quan=models.IntegerField(default=1)


class Cart(models.Model):
    cid=models.ForeignKey(Cakeitem,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    kg=models.IntegerField(default=1)
    quan=models.IntegerField(default=1)