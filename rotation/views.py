import json

from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from index.models import *


def get_all(request):
    rows = request.GET.get('rows', 2)
    page = request.GET.get('page', 1)
    st_list = list(Rotation.objects.all().order_by('id'))
    paginator = Paginator(st_list, int(rows))
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
        if isinstance(u, Rotation):
            return {
                'id': u.id,
                'desc': u.title,
                'date': u.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
                'status': u.status,
                'img_url': str(u.img_url),
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def edit(request):
    oper = request.POST.get('oper')
    desc = request.POST.get('desc')
    id = request.POST.get('id')
    status = request.POST.get('status')
    if oper == 'edit':
        with transaction.atomic():
            car = Rotation.objects.get(id=id)
            car.status = True if status == '1' else False
            car.title = desc
            car.save()
    elif oper == 'del':
        with transaction.atomic():
            Rotation.objects.get(id=id).delete()
    return HttpResponse()


@csrf_exempt
def add(request):
    title = request.POST.get('title')
    status = True if request.POST.get('status') == '1' else False
    pic = request.FILES.get('pic')
    Rotation.objects.create(title=title, status=status, img_url=pic)
    return HttpResponse()

