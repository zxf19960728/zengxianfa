import time
now= time.strftime("%y-%m-%d %H:%M:%S")  #年月日小写，日期大写
print(now)


#  zxf = input("请输入账号：")
for i in range(10):
    for j in range(i+1):
        with open("666.txt","a",encoding= "utf8") as res:
            res.write(now+"\n")  
            res.write("哈哈哈"+"\n")







