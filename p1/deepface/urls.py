from django.urls import path
from . import   views


urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('home',views.home,name='home'),
    path('camera_setting',views.camera_setting,name="camera_setting")
    ]