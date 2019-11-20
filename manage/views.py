from django.shortcuts import render, get_list_or_404
from api import models

# Create your views here.


def create(req):
    return render(req, 'manage/create.html', {'datas': list(models.Activity.objects.all())})


def display(req):
    return render(req, 'manage/display.html', {'datas': list(models.Activity.objects.all()), 'url': req.META.get("HTTP_HOST")})
