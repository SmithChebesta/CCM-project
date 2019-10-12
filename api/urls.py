
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/code', views.create_code, name='create_code'),
    path('create/activity', views.create_activity, name='create_activity'),
]
