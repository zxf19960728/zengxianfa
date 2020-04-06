import requests
from dbtools import Db

db =Db("192.144.148.91","ljtest","123456","lj123456")

url ="http://192.144.148.91:2333/login"
data= {"username":"langjin","password":"lj123456"}
res =requests.post(url=url,json=data)
token=res.json()["data"]["token"]
print(res.text)
print(token)
