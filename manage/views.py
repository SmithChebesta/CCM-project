from django.shortcuts import render, get_list_or_404
from api import models

# Create your views here.


def create(req):
    try:
        activity_data = get_list_or_404(models.Activity)
        return render(req, 'manage/create.html', {'datas': activity_data})
    except:
        return render(req, 'manage/create.html', {'datas': ''})


def display(req):
    try:
        activity_data = get_list_or_404(models.Activity)
        return render(req, 'manage/display.html', {'datas': activity_data})
    except:
        return render(req, 'manage/display.html', {'datas': ''})
