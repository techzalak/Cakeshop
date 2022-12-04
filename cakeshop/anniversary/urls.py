from django.urls import path

from . import views

urlpatterns = [
    path('',views.anni),
    path('<slug:data>',views.anni, name='annidata'),
    path('annidetail/<pid>', views.AnnidetView.as_view(), name="annidetail")
]