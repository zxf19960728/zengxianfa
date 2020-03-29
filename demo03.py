# #元组 下标
# a =(1,2,3,4,"哈哈哈",True,False,"嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎","嘎嘎",)
# print(a[-1])
# print(a[:3])
# print(a[4:8])

# # # # # print(a.index("哈哈哈"))
# # # # # print(a.count("嘎嘎"))


# # # # b =(a,"哈哈哈","嘻嘻","嘎嘎")
# # # # print(b[0][3])
# # # # print(a[1:-1])


# # # a =[1,2,3,4,"哈哈哈",True,False,"嘎嘎","嘎嘎","嘎嘎"]
# # # print(a[6])
# # # a.append("曾宪法")
# # # a.append(23.23)
# # # print(a)

# # # a.append("哈哈")
# # # print(a)
# # # a.insert(3,"张三")
# # # print(a)
# # # b =a.pop(5)#剪切
# # # print(a)
# # # print(b)

# # # c =a.pop(0)
# # # d =a.pop(0)
# # # print(c+d)
# # # print(c)
# # # print(d)

# # # # a.clear()
# # # # print(a)

# # # xx =["你好","真好"]
# # # a.extend(xx)
# # # print(a)
# # # a.insert(0,"我爱你")
# # # print(a)

# # # e =a.remove("张三")#  remove,remove,remove,remove,remove删除某个值，跟pop不一样，pop是剪切
# # # print(e)
# # # print(a)

# # # o =[1,0,True,False]# 0=false ,1=True
# # # h =o.count(0)
# # # print(h)
# # # print(len(a))











# # # # a =[1,2,3,4,"哈哈","嘻嘻",True,False]
# # # # a.append("append1")
# # # # a.append("append2")
# # # # print(a)
# # # # a.insert(4,"insert")
# # # # print(a)
# # # # b =a.pop(5)
# # # # print(a)
# # # # print(b)



# #字典的结构必须是：键值对  ：key：value
# a ={"name":"曾宪法",3:"嘻嘻","age":25}
# print(a)
# #取值
# print(a["name"],3,"age")
# #新增 
# a["high"] ="177cm"
# a["sex"] ="男"
# print(a)
#  #修改
# a["sex"]="女"
# a["high"]="190cm"
# print(a)

# b =a.get("name")
# print(b)
# print(a)
# c =a.pop("name")
# print(c)
# print(a)
# a.update(name="张三")
# print(a)


# print("------------------")

# print(a.get("name"))
# print(a["name"])

# print("------------------")

# print(a.get("name1"))
# # print(a["name1"])

# # del a["name"]
# # print(a)


# del(a["name"])
# print(a)



# a ={}
# a["name"] =str((input("请输入姓名:")))
# a["age"] = int((input("请输入年龄:")))
# a["sex"]= str((input("请输入性别：")))
# print(a)
# print(type(a))

name =(input("请输入你的姓名："))
age =(input("请输入你的年龄："))
sex =(input("请输入你的性别:"))
useinfo ={}
useinfo.update(name=name,age=age,sex=sex)
print(useinfo)