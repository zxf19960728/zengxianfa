import pymysql 
"""
导包
"""

test =pymysql.connect(host="111.229.214.158",user="root",password="123456",db="ZXF")
cursor = test.cursor() #获取游标
cursor.execute("select * from t_admin;")
res =cursor.fetchall()
for i in res:
    print(i)