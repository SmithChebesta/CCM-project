from django.shortcuts import render, get_object_or_404
from api import models

# Create your views here.


def create(req):
    return render(req, 'manage/create.html')


def display(req):

    return render(req, 'manage/display.html')
