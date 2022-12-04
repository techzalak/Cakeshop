from django.urls import path
from . import views

urlpatterns = [
    path('franadd/',views.frandata),
    path('',views.fadd),
    path('delete/<int:id>/',views.deletefdata, name="deletedata"),
    path('<int:id>/',views.updatefdata, name="updatedata"),
    path('franlogout/',views.flogout, name="franlogout")
]