from django.urls import path
from . import views

urlpatterns = [
    path('',views.graduation),
    path('<slug:data>',views.graduation, name='graduationdata'),
    path('graddetail/<pid>', views.GraddetView.as_view(), name="graddetail")
]