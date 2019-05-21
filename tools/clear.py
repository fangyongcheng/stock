import MySQLdb
import xlrd
"""综合清洗"""

sql="insert into yanglaoyuan_clear(cityname,name,address,tel,area) VALUES (%s,%s,%s,%s,%s)"
conn= MySQLdb.Connect(charset='utf8',host='localhost',user='root',passwd='123456',db='yanglaoyuan',port=3306)
cur=conn.cursor()

data = xlrd.open_workbook('合集.xlsx') # 打开xls文件
table = data.sheets()[0] # 打开第一张表
table1 = data.sheets()[1] # 打开第2张表
nrows = table.nrows
print(nrows)
l1=[]
l2=[]
l=[]
for i in range(nrows):   # 循环逐行打印
    if table.row_values(i)[0:4] not in l:
        l.append(table.row_values(i)[0:4])
        l1.append(table.row_values(i)[:])
for i in range(nrows):   # 循环逐行打印
    if table.row_values(i)[0:4] not in l:
        l.append(table.row_values(i)[0:4])
        l1.append(table.row_values(i)[:])
print(len(l))
print(len(l1))

for i in l1:
    cur.execute(sql,i)
conn.commit()