from django.shortcuts import render, redirect
from index.models import *
from rbac.permission import permission


def login(request):
    return render(request, 'loginform.html')


def login_logic(request):
    name = request.POST.get("name")
    pwd = request.POST.get('pwd')

    user = UserInfo.objects.filter(name=name, password=pwd).first()

    if not user:
        return render(request, "loginform.html", {'msg': "用户名或密码错误"})

    permission(user, request)

    return redirect("/cmfz/index/")
