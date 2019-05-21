from django.db.models import Count
from django.shortcuts import render,HttpResponse,redirect
from menu.models import StockCodeTXinlang
from login.models import Chouse,User

# Create your views here.

# 显示菜单页
def show_menu_views(request):
    areas=request.GET.get('area')
    codes=StockCodeTXinlang.objects.filter(positions=areas)
    return render(request,'menu.html',{"codes":codes})

# 显示个人页
def show_person_view(request):
    userid = request.session.get('userid')
    choose=Chouse.objects.filter(userid_id=userid)
    codes=[]
    for i in choose:
        i=StockCodeTXinlang.objects.get(code=i.code)
        if i:
            codes.append(i)
    return render(request,'private.html',{"codes":codes})

# 添加
def add_choose(request):
    userid = request.session.get('userid')
    user=User.objects.get(id=userid)
    code=request.GET.get('code')
    Chouse.objects.create(userid=user,code=code)
    return redirect(to='menu:menu')

# 删除
def del_choose(request):
    userid = request.session.get('userid')
    code = request.GET.get('code')
    Chouse.objects.filter(code=code).filter(userid=userid).delete()
    return redirect(to='menu:person')

# 地区
def area(request):
    codes = StockCodeTXinlang.objects.values('positions').annotate(Count('positions'))
    return render(request, 'area.html', {"codes": codes})

# 退出
def quit(request):
    del request.session['flag']
    return redirect('login:login')