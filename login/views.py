

# Create your views here.
import re
import requests
from django.shortcuts import render,redirect,HttpResponse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from redis import Redis

from login.models import User
# Create your views here.

url = "http://www.ip138.com/ips138.asp?ip=%s&action=2"
def login(request):
    name=request.COOKIES.get('userid')
    pwd=request.COOKIES.get('psw')
    user=User.objects.filter(username=name,password=pwd)
    if user:
        return redirect('main_app:main')
    else:
        return render(request, 'login.html')

def login_logic(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    user=User.objects.filter(username=name,password=pwd)
    if user:
        request.session['flag'] = 'ok'  # 记录下登录状态， OK时候登录，保持登录
        request.session['userid'] = user[0].id  # 记录下登录状态userid
        return HttpResponse('成功')
    else:
        return HttpResponse('用户名或密码错误！')

def login_ok(request):
    return redirect('menu:area')



def regist(request):
    return render(request,'register.html')
def registlogic(request):
    username=request.POST.get('username')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    print(username,phone,email,pwd)
    User.objects.create(username=username,phone=phone,email_addr=email,password=pwd)
    return redirect('login:login')
def usernameajax(request):
    username=request.GET.get('username')
    print(username)
    result=User.objects.filter(username=username)
    if result:
        return  HttpResponse('该用户名已注册')
    else:
        return HttpResponse('该用户名可用')