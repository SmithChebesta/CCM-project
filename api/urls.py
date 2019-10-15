
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('create/code', views.create_code, name='create_code'),
    path('create/activity', views.create_activity, name='create_activity'),
    path('user/signup', views.sign_up, name='signup'),
    path('user/logout', views.logout, name='logout'),
    path('user/login', views.login, name='login'),
    path('user/addcode', views.addcode, name='addcode'),
    path('user/getcode', views.user_used_code, name='getcode'),
]
