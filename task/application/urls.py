from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
   path('', views.get_intern_details, name='intern_details')
   
]