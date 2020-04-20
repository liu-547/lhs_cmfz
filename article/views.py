import json
import datetime
import os

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from redis import Redis

from index.models import *


def get_all_article(request):
    rows = request.GET.get('rows', 5)
    page = request.GET.get('page', 1)
    article_list = list(Article.objects.all().order_by('id'))
    paginator = Paginator(article_list, int(rows))
    try:
        rows = list(paginator.page(page).object_list)
    except:
        rows = list(paginator.page(int(page) - 1).object_list)
        page = int(page) - 1

    page_data = {
        'page': page,
        'total': paginator.num_pages,
        'records': paginator.count,
        'rows': rows
    }

    def mydefault(a):
        if isinstance(a, Article):
            return {
                'id': a.id,
                'title': a.title,
                'content': a.content,
                'cate': a.cate,
                'author': a.author,
                'publishtime': a.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


@csrf_exempt
def edit_article(request):
    id = request.POST.get('id')
    cate = request.POST.get('cate')
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    try:
        with transaction.atomic():
            art = Article.objects.get(id=id)
            art.content = content
            art.author = author
            art.title = title
            art.cate = cate
            art.save()
    except:
        return JsonResponse({'meg': 'faile'})
    return JsonResponse({'msg': 'success'})


@csrf_exempt
def add_article(request):
    cate = request.POST.get('cate')
    print(cate)
    title = request.POST.get('title')
    print(title)
    content = request.POST.get('content')
    author = request.POST.get('author')
    try:
        with transaction.atomic():
            Article.objects.create(title=title, cate=cate, author=author, content=content)
    except:
        return JsonResponse({'status': 'faile'})
    return JsonResponse({'status': 'success'})


@csrf_exempt
def del_article(request):
    oper = request.POST.get('oper')
    id = request.POST.get('id')
    if oper == 'del':
        with transaction.atomic():
            Article.objects.get(id=id).delete()
    return HttpResponse()


@xframe_options_sameorigin  # 允许页面嵌套时发起访问
@csrf_exempt
def upload_img(request):
    file = request.FILES.get("imgFile")

    if file:
        # 获取图片所在的服务的全路径
        img_url = request.scheme + "://" + request.get_host() + "/static/article_pic/" + str(file)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(pics=file)
    else:
        result = {"error": 1, "url": "上传失败"}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_all_img(request):
    pic_dir = request.scheme + "://" + request.get_host() + '/static/'
    pic_list = Pic.objects.all()
    rows = []
    for i in list(pic_list):
        # 获取图片的后缀
        print(i.pics.url)
        path, pic_suffix = os.path.splitext(i.pics.url)
        rows.append({
            "is_dir": False,
            "has_file": False,
            "filesize": i.pics.size,
            "dir_path": "",
            "is_photo": True,
            "filetype": pic_suffix,
            "filename": i.pics.name,
            "datetime": "2018-06-06 00:36:39"
        })

    data = {
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": pic_dir,
        "total_count": len(pic_list),
        "file_list": rows

    }
    return HttpResponse(json.dumps(data), content_type="application/json")
