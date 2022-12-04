from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.pay),
    path('paymentin/', views.payind),
    path('charge/', views.charge, name="charge"),
    path('chargeind/', views.chargeind, name="chargeind"),
    path('success/<str:args>/', views.success, name="success"),
]
