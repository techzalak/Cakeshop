from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.intro),
    path('contactus/',views.contact),
    path('discounts/',views.offer),
    path('faq/',views.faq),
    path('franchise/',views.fran),
    path('homebaker/',views.homebake),
    path('custlogin/',views.custlogin),
    path('logout/',views.user_logout, name='logout'),
    path('homemade/',views.home),
    path('homemade/<slug:data>',views.home, name='homemade'),
    path('yearlysub/',views.year),
    path('homepayment/',views.payhome)
]