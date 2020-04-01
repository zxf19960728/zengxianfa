#字典的结构必须是：键值对  ：key：value
a ={"name":"曾宪法",3:"嘻嘻","age":25}
print(a)
#取值
print(a["name"])
print(a[3])




light={"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        print(i,light[i]-j)

