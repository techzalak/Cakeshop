"""cakeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.urls') ),
    path('birthdays/',include('birthdays.urls')),
    path('pastries/',include('pastries.urls')),
    path('graduation/', include('graduation.urls')),
    path('kids/', include('kids.urls')),
    path('anniversary/', include('anniversary.urls')),
    path('franprofile/',include('franprofile.urls')),
    path('cart/', include('cart.urls')),
    path('payment/', include('payorder.urls')),
    path('homeprofile/', include('homeprofile.urls')),
    path('brands/', include('brands.urls')),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)