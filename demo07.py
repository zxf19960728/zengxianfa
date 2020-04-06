# import  dbtools
from dbtools import Db
import requests

# db=Db("111.229.214.158","root","123456","zxftest")
# a=db.chaxun("select * from t_class;")
# print(a)
# for i in a:
#     print(i)
# b = input("请输入:")
# a = chaxun(b)
# for i in a:
#     print(i)
url = "http://192.144.148.91:2333/login"

payload = "{\r\n\"username\":\"langjin\", \r\n\"password\":\"lj123456\" \r\n}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "ccce9c9e-0762-4efb-8a2f-594bb16f7671"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)