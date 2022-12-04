from django.urls import path
from . import views

urlpatterns = [
    path('brmonginis/',views.b_monginis, name='Monginis'),
    path('brmonginis/<slug:data>',views.b_monginis, name='b_monginisdata'),
    path('brribbal/',views.b_ribbal, name="Ribbons and Balloons"),
    path('brribbal/<slug:data>',views.b_ribbal, name='b_ribbaldata'),
    path('brmerwans/',views.b_merwans, name="Merwans"),
    path('brmerwans/<slug:data>',views.b_merwans, name='b_merwansdata'),
    path('brheaven/',views.b_heaven, name="7th Heaven"),
    path('brheaven/<slug:data>',views.b_heaven, name='b_heavendata'),
    path('brbasrob/',views.b_basrob, name="Baskin-Robins"),
    path('brbasrob/<slug:data>',views.b_basrob, name='b_basrobdata'),
    path('brlgateau/',views.b_lgateau, name="Le gateau"),
    path('brlgateau/<slug:data>',views.b_lgateau, name='b_lgateaudata'),
    path('mondetail/<pid>', views.MondetView.as_view(), name="mondetail")
]