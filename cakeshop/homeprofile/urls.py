from django.urls import path
from . import views

urlpatterns = [
    path('homeadd/',views.homedata),
    path('',views.homeadd),
    path('delete/<int:id>/',views.deletehdata, name="deletehdata"),
    path('<int:id>/',views.updatehdata, name="updatehdata"),
    path('hlogout/',views.hlogout, name="hlogout"),


]