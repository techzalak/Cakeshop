from django.contrib import admin
from .models import SignCustomer, SignFranchise,Signhome,Cakeitem
# Register your models here.

@admin.register(SignFranchise)
class Fransignadmin(admin.ModelAdmin):
    list_display=('user','brand','address','pin','gst','name','mobile')

@admin.register(Signhome)
class Homesignadmin(admin.ModelAdmin):
    list_display=('user','address','pin','fss','name','mobile')

@admin.register(Cakeitem)
class Cakeitemadmin(admin.ModelAdmin):
    list_display=('id','user','brand','name','cimg','category','price500','price1','price2','price3','des')

@admin.register(SignCustomer)
class Customersignadmin(admin.ModelAdmin):
    list_display=('user','address','pin','name','mobile','yearlsub')