
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.create, name='create'),
    path('display/', views.display, name='display'),
]
