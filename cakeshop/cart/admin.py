from django.contrib import admin

# Register your models here.

from .models import Cartitem, Cart
# Register your models here.
@admin.register(Cartitem)

class CartAdmin(admin.ModelAdmin):
  list_display = ('cid','kg','quan')

@admin.register(Cart)

class CartAdmin(admin.ModelAdmin):
  list_display = ('cid','user','kg','quan')