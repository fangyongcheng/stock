"""
爬取新浪财经股票代码及名字存库
"""
import re
import requests
import json

import time
from lxml import etree
import MySQLdb


conn=MySQLdb.Connect(user="root",password="123456",db="stock",port=3306,charset="utf8")
cursor=conn.cursor()


sql="insert into stock_code_t_xinlang(name,code,positions) VALUES (%s,%s,%s)"

def getData(page,i):
    try:

        url = "http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=%s&num=40&sort=symbol&asc=1&node=%s&symbol=&_s_r_a=init" % (
        page, i[2])
        res = requests.get(url,timeout=1).text
        print(res)
        if res == "null":
            return 1
        res = res.split("},{")
        for j in res:
            code = re.findall('symbol:"(.*?)"', j)
            name = re.findall('name:"(.*?)"', j)
            positions = i[0]
            cursor.execute(sql,[code, name, positions])
            conn.commit()
    except:
        pass

get_city="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodes"
res=requests.get(url=get_city).text.split("地域板块")[1]
res=res.split("cn")[0][3:-13]
res='['+res+']'
res=json.loads(res)

with open("地区.json",'w') as f:
    json.dump(res,f)


for i in res:
    with open("完成地区.json", 'a+') as f:
        f.write(str(i)+'\n')
    page=0
    time.sleep(2)
    while 1:
        page += 1
        r=getData(page,i)
        if r==1:
            break


#
# # res.encoding="gb2312"
# print(res)
# conn.commit()
# cursor.close()
# conn.close()