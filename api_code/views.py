from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import code_generator
from . import models
import datetime
# Create your views here.


@csrf_exempt
def create(req):

    if req.method == 'POST':
        code_list = code_generator.get_code(int(req.POST.get('amount')), int(
            req.POST.get('length')), req.POST.get('prefix'))

        Activity = models.Activity(
            atvcode=req.POST.get('atvcode'), name='Test activity name')
        Activity.save()

        for code in code_list:
            Code = models.Code(exp=datetime.datetime.now(), point='3', used=False,
                               code=code)
            Code.atvcode = models.Activity.objects.get(
                atvcode=req.POST.get('atvcode'))
            Code.save()
        return HttpResponse(status=200)
