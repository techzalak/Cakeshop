from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.birthcakes),
    path('<slug:data>',views.birthcakes, name='birthcakesdata'),
    path('birthdaydetail/<pid>', views.BirthdetView.as_view(), name="birthdaydetail")
]