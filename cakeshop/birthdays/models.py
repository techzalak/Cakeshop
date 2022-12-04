from django.db import models

# Create your models here.
class Birthday(models.Model):
    bpid=models.CharField(max_length=10,unique=True, default="none")
    bname= models.CharField(max_length=30)
    bimage=models.ImageField(null=True, blank=True,upload_to='images/')
    bdescrip=models.CharField(max_length=100)
    bprice500=models.IntegerField(null=True,blank=True)
    bprice1=models.IntegerField(null=True, blank=True)
    bprice2=models.IntegerField(null=True, blank=True)

    