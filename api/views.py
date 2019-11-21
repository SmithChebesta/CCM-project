from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse

from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from . import code_generator
from . import models
from client import models as client_models
import datetime
import unicodecsv as csv


@csrf_exempt
def create_code(req):
    if req.method == 'POST':
        code_list = code_generator.get_code(int(req.POST.get('amount')), int(
            req.POST.get('length')), req.POST.get('prefix'))

        for code in code_list:
            Code = models.Code(exp=req.POST.get('exp'), point=float(req.POST.get('point')), used=False,
                               code=code)

            Code.atvname = get_object_or_404(
                models.Activity, pk=req.POST.get('atvname'))
            Code.save()

        return HttpResponse(status=200)


@csrf_exempt
def create_activity(req):

    if req.method == 'POST':
        Activity = models.Activity(
            atvname=req.POST.get('atvname'), date=req.POST.get('exp'), status=True, place=req.POST.get('place'))
        Activity.save()

        return HttpResponse(status=200)


@csrf_exempt
def sign_up(req):
    if req.method == 'POST':
        # check if user is already exist
        try:
            user = User.objects.get(username=req.POST['student_id'])
            return JsonResponse({'error': 'User already exist'}, status=400)
        except User.DoesNotExist:
            #  register new user
            user = User.objects.create_user(
                username=req.POST['student_id'], first_name=req.POST['name'])
            user_profile = client_models.UserProfile(
                user=user, faculty=req.POST['faculty'])
            user_profile.save()
            auth.login(req, user)
            return JsonResponse({'student_id': req.POST['student_id'], 'name': req.POST['name'], 'faculty': req.POST['faculty']}, status=200)


@csrf_exempt
def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        return HttpResponse(status=200)


@csrf_exempt
def login(req):
    if req.method == 'POST':
        try:
            user = User.objects.get(username=req.POST['student_id'])
            auth.login(req, user)
            return JsonResponse({'name': user.get_username()}, status=200)
        except:
            return HttpResponse(status=400)


@csrf_exempt
def addcode(req):
    if req.method == 'POST':
        try:
            code = models.Code.objects.get(pk=req.POST['code'])
            if code.used:
                return JsonResponse({'error': 'Code already used'}, status=400)
            else:
                code.used_at = timezone.datetime.now()
                code.used_by = req.user
                code.used = True
                code.save()
                return HttpResponse(status=200)
        except:
            return JsonResponse({'error': 'Wrong code'}, status=400)


@csrf_exempt
def user_used_code(req):
    code_list = req.user.code_set.all()
    json = {'data': list(code_list.values('point', 'used_at', 'atvname'))}

    return JsonResponse(json, status=200)


@csrf_exempt
def update_status_atv(req):
    if req.method == 'POST':
        atvname = req.POST.get('atvname')
        atv = models.Activity.objects.get(pk=atvname)
        atv.status = not atv.status
        atv.save()
        # return HttpResponse(models.Activity.objects.get(pk=atvname).status)
        return JsonResponse({'status': models.Activity.objects.get(pk=atvname).status}, status=200)


@csrf_exempt
def get_csv(req):
    if req.method == 'GET':
        atvname = req.GET.get('atvname')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="activity_summary.csv"'
        writer = csv.writer(response, encoding='utf-8-sig')
        writer.writerow(
            ['ลำดับ', 'ชื่อกิจกรรม', 'รหัสผู้เข้าร่วม', 'วันที่กรอกรหัส'])
        x = 1
        for code in models.Code.objects.all():
            if(str(code.atvname) == atvname and code.used):
                writer.writerow([x, str(code.atvname), str(
                    code.used_by), str(code.used_at.strftime("%m/%d/%Y, %H:%M:%S"))])
                x += 1

        return response
        # return JsonResponse({'status': models.Activity.objects.get(pk=atvname).status}, status=200)


@csrf_exempt
def get_atvcode(req):
    if req.method == 'GET':
        atvname = req.GET.get('atvname')
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="activity_code.csv"'
        writer = csv.writer(response, encoding='utf-8-sig')
        writer.writerow(
            ['ลำดับ', 'ชื่อกิจกรรม', 'รหัสกิจกรรม', 'สถานะ'])
        x = 1
        for code in models.Code.objects.all():
            if(str(code.atvname) == atvname):
                writer.writerow([x, str(code.atvname), str(
                    code.code), str(code.used)])
                x += 1

        return response
