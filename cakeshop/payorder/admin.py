from django.contrib import admin
from .models import Cakeorder
# Register your models here.
@admin.register(Cakeorder)

class CartAdmin(admin.ModelAdmin):
  list_display = ('cid','user','kg','quan', 'addr', 'order_date', 'delivery_date')