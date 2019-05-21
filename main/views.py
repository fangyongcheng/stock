from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from login.models import Chouse
from menu.models import StockCodeTXinlang
import requests
# Create your views here.

# 链接到详情
def show_main_views(request):
    code=request.GET.get("code")
    code=StockCodeTXinlang.objects.get(code=code)
    return render(request,'main.html',{"code":code})

# 查询
def look_view(request):
    flag = request.GET.get("flag")
    keyword = request.GET.get("keyword")
    try:
        if flag=="1":
            code = StockCodeTXinlang.objects.get(name__icontains=keyword)
        if flag=="2":
            code = StockCodeTXinlang.objects.get(code=keyword)
        # if code
    except:
        return HttpResponse("没找到！")
    return render(request, 'main.html', {"code": code})


# 获得一月数据展示echarts
def get_data(request):
    flag = request.GET.get("flag")
    code = request.GET.get("code")
    url="https://quotes.sina.cn/cn/api/json_v2.php/CN_MarketDataService.getKLineData?symbol=%s&scale=30&ma=no&datalen=1023"%code
    res=requests.get(url).json()
    l=[]
    for i in res:
        l.append([i["day"],i["open"],i["close"],i["high"],i["low"]])
    return JsonResponse(l,safe=False)

# 获得一月数据展示echarts折线
def get_data_z(request):
    userid=request.session.get("userid")
    choose = Chouse.objects.filter(userid_id=userid)
    data=[]
    name=[]
    for i in choose:
        i = StockCodeTXinlang.objects.get(code=i.code)
        if i:
            url="https://quotes.sina.cn/cn/api/json_v2.php/CN_MarketDataService.getKLineData?symbol=%s&scale=60&ma=no&datalen=1023"%i.code
            res=requests.get(url).json()[150:]
            l_data=[]
            l_time=[]
            name.append(i.name)
            for j in res:
                l_data.append(j["high"])
                l_time.append(j["day"])
            data.append(l_data)
    time=l_time
    datas={"data":data,
           "time":time,
           "name":name
           }

    return JsonResponse({"data":datas},safe=False)

