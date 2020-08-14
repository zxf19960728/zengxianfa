import pymysql
'''
导包：pymysql
'''

# db = pymysql.connect(host="111.229.214.158",user="root",password="123456",db="ZXF")
# cursor = db.cursor()  #获取游标
# cursor.execute("select * from t_admin;")
# res =cursor.fetchall()
# for i in res:
#     print(i)

def chaxun(sql):
    db = pymysql.connect(host="111.229.214.158",user="root",password="123456",db="ZXF")
    cursor = db.cursor()  #获取游标
    try:
        cursor.execute(sql)
        res =cursor.fetchall()
        return res
    except:
        return "sql语句写错了"

a = "select * from t_admin;"
b =chaxun(a)
for i in b:
    print(i)

