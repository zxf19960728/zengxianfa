# import time
# import random
# b=[]
# c=[]
# d =0
# while d<10:
#     a=random.randint(1,10)
#     if a>5:
#         b.append(a)
#     else:
#         c.append(a)
#     d =d+1 
# print(b)
# print(c)
       

# print(a)



import pymysql

db=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="zxftest")
cur=db.cursor()
cur.execute("select * from t_studnet")
res =cur.fetchall()
print(res)