from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('details', views.get_intern_details, name='intern_details')
]