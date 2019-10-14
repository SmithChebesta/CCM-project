from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import code_generator
from . import models
import datetime


@csrf_exempt
def create_code(req):
    if req.method == 'POST':
        code_list = code_generator.get_code(int(req.POST.get('amount')), int(
            req.POST.get('length')), req.POST.get('prefix'))

        for code in code_list:
            Code = models.Code(exp=req.POST.get('exp'), point=float(req.POST.get('point')), used=False,
                               code=code)

            Code.atvcode = get_object_or_404(
                models.Activity, pk=req.POST.get('atvcode'))
            Code.save()

        return HttpResponse(status=200)


@csrf_exempt
def create_activity(req):

    if req.method == 'POST':

        Activity = models.Activity(
            atvcode=req.POST.get('atvcode'), name=req.POST.get('name'), date=req.POST.get('date'), status=True, place=req.POST.get('place'))
        Activity.save()

        return HttpResponse(status=200)


@csrf_exempt
def sign_up(req):
    if req.method == 'POST':
        # Activity = models.Activity(
        #     atvcode=req.POST.get('atvcode'), name=req.POST.get('name'), date=req.POST.get('date'), status=True, place=req.POST.get('place'))
        # Activity.save()

        return JsonResponse({'student_id': req.POST['student_id'], 'name': req.POST['name'], 'faculty': req.POST['faculty']})
