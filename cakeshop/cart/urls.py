from django.urls import path
from . import views

urlpatterns = [
    path('addcart/',views.cartdata, name="add_cart"),
    path('',views.showcart, name="cart"),
    path('pluscart/',views.pluscart, name="pluscart"),
    path('minuscart/', views.minuscart),
    path('removeitem/', views.removeitem),
]