import re
from index.get_code import random_code
from index.send_message import YunPian
from redis import Redis
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cfmz.settings import API_KEY


def index(request):
    return render(request, 'main.html')


def login(request):
    return render(request, 'login.html')


@csrf_exempt
def get_code(request):
    redis = Redis(host="localhost", port=6379)
    phone_num = request.POST.get('mobile')
    is_pnum = re.match(r"^1[35678]\d{9}$", phone_num)
    if is_pnum:
        saved_code = redis.get(f'{phone_num}_1')
        if saved_code:
            return JsonResponse({'status': 0})
        code = random_code()
        print(code)
        yun_pian = YunPian(API_KEY)
        yun_pian.send_message(phone_num, code)

        redis.set(f"{phone_num}_1", code, 60)
        redis.set(f"{phone_num}_2", code, 300)

        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def check_user(request):
    redis = Redis(host="localhost", port=6379)
    phone_num = request.GET.get('mobile')
    code = request.GET.get('code')
    phone_result = re.match(r"^1[35678]\d{9}$", phone_num)
    code_result = re.match(r"\d{5}$", code)
    if phone_result and code_result:
        try:
            saved_code = redis.get(f'{phone_num}_2')
            if saved_code.decode() == code:
                return JsonResponse({'status': 1})
        except BaseException as error:
            return JsonResponse({'status': 0, 'msg': '验证码失效'})
        return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 0})
