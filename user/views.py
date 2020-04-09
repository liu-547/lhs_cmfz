import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
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


def add_user(request):
    return


def edit_user(request):
    return


def get_registinfo(request):
    return


def get_usermap(request):
    return
