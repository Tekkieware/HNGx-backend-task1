from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
   
   path('', views.create_user, name='create_user'),
   path('/<user_id>', views.tweak_user, name='tweak_user'),
   path('/intern_details', views.get_intern_details, name='intern_details'),
   
]