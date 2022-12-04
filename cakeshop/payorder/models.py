from django.db import models
from django.db.models.fields.related import ForeignKey
from homepage.models import Cakeitem
from django.contrib.auth.models import User
# Create your models here.
class Cakeorder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cid=models.ForeignKey(Cakeitem,on_delete=models.CASCADE)
    kg=models.IntegerField(default=1)
    quan=models.IntegerField(default=1)
    addr=models.CharField(max_length=200, default="None")
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date=models.CharField(max_length=150, default="None")