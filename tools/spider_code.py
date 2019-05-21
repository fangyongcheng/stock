"""
爬取东方财经股票代码及名字存库
"""
import requests
from lxml import etree
import MySQLdb


conn=MySQLdb.Connect(user="root",password="123456",db="stock",port=3306,charset="utf8")
cursor=conn.cursor()


sql="insert into stock_code_t(name,code,positions) VALUES (%s,%s,%s)"


url="http://quote.eastmoney.com/stock_list.html#sz"

res=requests.get(url)
res.encoding="gb2312"
res=res.text
html=etree.HTML(res)
code_list=html.xpath("//li//text()")
l=code_list[130:]
for i in l:
    i=i.replace(")",'')
    i=i.split("(")
    if len(i)==2:
        i.append("深圳")
        cursor.execute(sql,i)
conn.commit()
cursor.close()
conn.close()