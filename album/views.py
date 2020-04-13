import json

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from index.models import *
from mutagen.mp3 import MP3


def get_all_album(request):
    rows = request.GET.get('rows', 5)
    page = request.GET.get('page', 1)
    album_list = list(Album.objects.all().order_by('id'))
    print(album_list)
    paginator = Paginator(album_list, int(rows))
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

    def mydefault(a):
        if isinstance(a, Album):
            return {
                'id': a.id,
                'title': a.title,
                'score': a.score,
                'publishDate': a.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
                'author': a.author,
                'cover': str(a.img_src),
                'broadcast': a.broadcast,
                'count': a.chapter_count,
                'content': a.content,
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


def get_all_chapter(request):
    albumid = request.GET.get('albumId')
    rows = request.GET.get('rows', 2)
    page = request.GET.get('page', 1)
    chapter_list = list(Chapter.objects.filter(album_id=albumid).order_by('id'))
    paginator = Paginator(chapter_list, int(rows))
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

    def mydefault(c):
        if isinstance(c, Chapter):
            return {
                'id': c.id,
                'title': c.title,
                'curl': str(c.url),
                'size': c.size,
                'duration': c.time_long,
            }

    data = json.dumps(page_data, default=mydefault)
    return HttpResponse(data)


def chapter_count(a_id):
    count = len(list(Chapter.objects.filter(album_id=a_id)))
    try:
        with transaction.atomic():
            album = Album.objects.get(id=a_id)
            album.chapter_count = count
            album.save()
    except Exception as tip:
        print(tip)
    return count


@csrf_exempt
def edit_album(request):
    oper = request.POST.get('oper')
    id = request.POST.get('id')
    title = request.POST.get('title')
    score = request.POST.get('score')
    author = request.POST.get('author')
    broadcast = request.POST.get('broadcast')
    publishdate = request.POST.get('publishDate')
    content = request.POST.get('content')
    # cover = request.FILES.get('cover')
    if oper == 'edit':
        with transaction.atomic():
            album = Album.objects.get(id=id)
            album.title = title
            album.score = score
            album.author = author
            album.broadcast = broadcast
            album.publish_time = publishdate
            album.content = content
            # album.img_src = cover
            album.save()
    elif oper == 'del':
        with transaction.atomic():
            Album.objects.get(id=id).delete()
    return HttpResponse()


@csrf_exempt
def edit_chapter(request):
    oper = request.POST.get('oper')
    id = request.POST.get('id')
    title = request.POST.get('title')
    if oper == 'edit':
        with transaction.atomic():
            chapter = Chapter.objects.get(id=id)
            chapter.title = title
            # album.img_src = cover
            chapter.save()
    elif oper == 'del':
        with transaction.atomic():
            Chapter.objects.get(id=id).delete()
    return HttpResponse()


@csrf_exempt
def add_album(request):
    with transaction.atomic():
        title = request.POST.get('title')
        print(title)
        score = request.POST.get('score')
        author = request.POST.get('author')
        broadcast = request.POST.get('broadcast')
        count = request.POST.get('count')
        content = request.POST.get('content')
        cover = request.FILES.get('cover')
        print(cover)
        Album.objects.create(title=title, score=score, author=author, broadcast=broadcast, chapter_count=count,
                             content=content, img_src=cover)
        return HttpResponse()


@csrf_exempt
def add_chapter(request):
    with transaction.atomic():
        al_id = request.GET.get('albumId')
        print(al_id)
        title = request.POST.get('title')
        audio = request.FILES.get('audio')
        # print(title, audio)
        # 音频大小
        size = audio.size

        # 音频时长
        audio_mp3 = MP3(audio)
        duration = audio_mp3.info.length
        print(size, duration)
        Chapter.objects.create(title=title, size=size, time_long=duration,
                               url=audio, album_id=al_id)
    return HttpResponse()
