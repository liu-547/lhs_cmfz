import json
import datetime
from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.models import *


def get_alluser(request):
    rows = request.GET.get('rows', 5)
    page = request.GET.get('page', 1)
    user_list = list(User.objects.all().order_by('id'))
    print(user_list)
    paginator = Paginator(user_list, int(rows))
    try:
        rows = list(paginator.page(page).object_list)
    except Exception as tips:
        print(tips)
        rows = list(paginator.page(int(page) - 1).object_list)
        page = int(page) - 1

    page_data = {
        'page': page,
        'total': paginator.num_pages,
        'records': paginator.count,
        'rows': rows
    }

    def mydefault(u):
        if isinstance(u, User):
            return {
                'id': u.id,
                'name': u.name,
                'religions_name': u.religions_name,
                'regist_time': u.regist_time.strftime("%Y-%m-%d %H:%M:%S"),
                'status': u.status,
                'img_url': str(u.img_src),
                'email': u.email,
                'detail': u.details,
                'addr': u.address,
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def add_user(request):
    with transaction.atomic():
        name = request.POST.get('name')
        print(name)
        status = True if request.POST.get('status') == '1' else False
        pic = request.FILES.get('pic')
        religions_name = request.POST.get('religions_name')
        password = request.POST.get('password')
        address = request.POST.get('address')
        details = request.POST.get('details')
        email = request.POST.get('email')
        User.objects.create(name=name, status=status, img_src=pic, religions_name=religions_name,
                            password=password, address=address, details=details, email=email)
        return HttpResponse()


@csrf_exempt
def edit_user(request):
    oper = request.POST.get('oper')
    name = request.POST.get('name')
    religions_name = request.POST.get('religions_name')
    details = request.POST.get('details')
    email = request.POST.get('email')
    id = request.POST.get('id')
    # status = request.POST.get('status')
    if oper == 'edit':
        with transaction.atomic():
            user = User.objects.get(id=id)
            # user.status = True if status == '1' else False
            user.name = name
            user.religions_name = religions_name
            user.details = details
            user.email = email
            user.save()
    elif oper == 'del':
        with transaction.atomic():
            User.objects.get(id=id).delete()
    return HttpResponse()


@csrf_exempt
def get_registinfo(request):
    today = datetime.datetime.now()
    day1 = (today + datetime.timedelta(days=-6)).strftime('%Y-%m-%d')
    day2 = (today + datetime.timedelta(days=-5)).strftime('%Y-%m-%d')
    day3 = (today + datetime.timedelta(days=-4)).strftime('%Y-%m-%d')
    day4 = (today + datetime.timedelta(days=-3)).strftime('%Y-%m-%d')
    day5 = (today + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
    day6 = (today + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
    user = User.objects.all()
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    for u in user:
        if u.regist_time.strftime('%Y-%m-%d') == day1:
            count1 += 1
        if u.regist_time.strftime('%Y-%m-%d') == day2:
            count2 += 1
        if u.regist_time.strftime('%Y-%m-%d') == day3:
            count3 += 1
        if u.regist_time.strftime('%Y-%m-%d') == day4:
            count4 += 1
        if u.regist_time.strftime('%Y-%m-%d') == day5:
            count5 += 1
        if u.regist_time.strftime('%Y-%m-%d') == day6:
            count6 += 1
        if u.regist_time.strftime('%Y-%m-%d') == today.strftime('%Y-%m-%d'):
            count7 += 1
    data = {"x": [1, 2, 3, 4, 5, 6, 7], "y": [count1, count2, count3, count4, count5, count6, count7]}
    return JsonResponse(data)


def get_usermap(request):
    return
