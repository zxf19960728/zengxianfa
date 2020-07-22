# a=1
# b=2
# if b==2:
#     print("666")

# if a>b:
#     print("a大于b")
# else:
#     print("b大于a")

# age=int(input("请输入你的年龄："))
# if age>60:
#     print("您年级挺大了")
# elif age>40:
#     print("您工作应该很累吧")
# elif age>20:
#     print("年轻真好")
# else:
#     print("你还小")

# a ="你"
# if a in "我":
#     print("yes")
# else:
#     print("no")

# a =input("请输入：")
# print(type(a))
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789,77":
#     a= int(a)
# else:
#     print("请输入数字！")
#     exit()
# if a>10:
#     print("你真棒")
# else:
#     print("加油哦")

# a ={}
# print(type(a))
# if type(a) is int:
#     print("是数字")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")

# a =1
# while a<10:
#     print("+1",a)
#     a =a+1

 high={}
# low={}
# studentlist = ["张三","李四","王五","小六","高琪","兰南巴","吴勇","狗十","王麻子","刘峰"]
# a =0
# while a< len(studentlist):
#     print(a)
#     a =a +1
#     chengji =int(input("请输入"+studentlist[a]+"成绩:"))
#     if chengji>=60:
        high[studentlist[a]]=chengji
    else:
        low[studentlist[a]] =chengji
    a =a+1
print("大于60的：",high)
# print("小于60的：",low)


# a =["张三","李四","王五","小六","高琪","兰南巴","吴勇","狗十","王麻子","刘峰"]
# for i in a:
#     print(i)
# b =list(range(100))
# print(b)

# for i in range(0,10):
#     print(i)

# b = list(range(0,100,4))
# print(b)

# high={}
# low={}
# studentlist = ["张三","李四","王五","小六","高琪","兰南巴","吴勇","狗十","王麻子","刘峰"]
# for i in studentlist:
#     chengji =int(input("请输入"+i+"成绩:"))
#     if chengji>=60:
#         high[i]=chengji
#     else:
#         low[i] =chengji
# print("大于60的：",high)
# print("小于60的：",low)


# a ="你好呀，您再做什么？"
# for i in a:
#     print(i)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"X",j,"=",i*j,end=" ")
#     print()






# high={}
# low={}
# student = ["张三","李四","王五","小六","高琪","兰南巴","吴勇","狗十","王麻子","刘峰"]
# for i in student:
#     chengji =int(input("请输入"+i+"成绩:"))
#     if chengji>=60:
#         high[i]=chengji
#     else:
#         low[i] =chengji
# print("大于60的：",high)
# print("小于60的：",low)
# high={}
# low={}
# student = ["张三","李四","王五","小六","高琪","兰南巴","吴勇","狗十","王麻子","刘峰"]
# for i in student:
#     chengji =int(input("请输入"+i+"成绩:"))
#     if chengji >=60:
#        high[i]=chengji
#     else:
#        low[i]=chengji
# print("大于60的成绩：",high)
# print("小于60的成绩：",low)


# a= tuple(range(1,100,1))
# print(type(a))
# print(a)
# for i in a:
#     print(i)

# a=0
# while a<30:
#     for i in range(30,0,-1):
#         print(a)
#         a =a+1



# light={"红灯":30,"绿灯":35,"黄灯":3}
# for i in light: #这里的i是key
#     for j in range(light[i]):#这里的j是valus，light[i]=30；
#         print(i,light[i]-j)



# for i in range(100):
#     if i==[20]:
#         continue   #continue 跳出本次循环 
#     print(i)
    
# def chengfa(a,b):
#     """两个数相乘"""
#     if type(a) is int and type(b) is int:
#         print(a*b)
#     else:
#         print("您的输入有误，请输入整数！")



# e =int(input("请输入:"))
# d =int(input("请输入:"))
# chengfa("哈",23)

# a =[1,2,3,4,1,2,1]
# x =a.index(2) #x=1
# print(x)
# if x ==1:
# return a[x]


# try:
#     print("bbaba "+1)
# except:
#     print("写错了")
    



