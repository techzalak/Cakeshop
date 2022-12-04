from django.urls import path
from . import views

urlpatterns = [
    path('',views.kidcake),
    path('kiddetail/<pid>', views.KiddetView.as_view(), name="kiddetail"),
    path('<slug:data>',views.kidcake, name='kidcakedata'),
]