# # # # '''print("hello world") #字符串
# # # # print("我真帅") #字符串
# # # # print(2333) #整数
# # # # print(23.23) #小数
# # # # print(True) #布尔值
# # # # print(()) #元组
# # # # print([]) #数组
# # # # print({}) #字典'''




# # # # '''
# # # # a ="张三"
# # # # b ="李四"
# # # # print(a,b)'''

# # # # # a =int(input("请输入:"))
# # # # # b =int(input("请输入:"))
# # # # # print("输出int：",a+b)


# # # # #数据格式的转换



# # # # # c =type("曾宪法")
# # # # # print(c)

# # # # '''print (type("曾")) #字符串 str
# # # # print (type(2333)) #整数 int
# # # # print (type(23.23)) #小数 float
# # # # print (type(True)) #布尔值 bool
# # # # print (type(()))   #元组 tuple
# # # # print (type([]))   #数组 list
# # # # print (type({}))   #字典 dict'''

# # # # # a = bool("2333")
# # # # # print (type(a))





# # # # # a =float (input("请输入："))
# # # # # b =float (input("请输入："))
# # # # # print("输出上面的input获取的内容:",a+b)
# # # # # print(type(a+b))





# # # # # a ='sdfjasjl;asdjkflasjlfdjas'
# # # # # print(len(a))


# # # # # a = input('')
# # # # # b = input('')
# # # # # print(len(a+b))



# # # # # a =input("请输入：")
# # # # # b =input("请输入：")
# # # # # print("两段字段的长度是",len(a)+len(b))







# # # # a = int(input ("请输入你的体重："))
# # # # if a<90:
# # # #     print("你太瘦了")
# # # # elif a>90 and a< 120:
# # # #     print ("你的体重正常")
# # # # else:
# # # #     print("你太胖了")


# # # # a =(1,2,3,4,5,6,7,8,"哈哈哈","嘻嘻",8,8,8,8,8,8,8,8)
# # # # print(a.index("哈哈哈"))
# # # # print(a[1])
# # # # print(a.count(8))



# # # # # 元组 下标，从0开始编号

# # # # # a =("曾宪法",2333,23.23,"哈哈哈",True,"哈哈哈","哈哈哈","哈哈哈","哈哈哈","哈哈哈",False)
# # # # # print(a[3])

# # # # # print (a.count("哈哈哈"))

# # # # # print(a.index(True))




# # # # b =(1)
# # # # if b<10:
# # # #     print("不正确")



# # # # a = int(input("请输入a的值："))
# # # # b = int(input("请输入b的值："))
# # # # print("输出a+b的值",a+b)



# # # print(type(2333))
# # # print(type("666"))
# # # print(type(True))
# # # print(type(()))
# # # print(type([]))
# # # print(type({}))
# # # print(type(23.23))


# # # # a =int("哈哈哈")
# # # # print(a)
# # # # print(type(a))

# # # b = float("2333")
# # # print(b)
# # # print(type(b))

# # # print(type(None))


# # # c =int(23.23)
# # # print(c)
# # # print(type(c))

# # # a =float(input("请输入:"))
# # # b =float(input("请输入:"))
# # # print("输出input的值",a+b)

# # b =(("哈哈哈哈哈哈哈哈哈哈啊啊哈","我的"))
# # print(len(b))
# # print(type(b))


# # # c =len("哈哈哈哈哈哈哈哈哈哈啊啊哈")
# # # print(c)




# a =input("请输入：")
# b =input("请输入：")
# print("输出input的值",len(a)+len(b))


# a = int(6)
# b =int(10)
# print(a+b)
# print(type(a+b))

# a =(1,2,3,4,5,6,"思考","哈哈","哈哈",True,False,2.333,)
# print(a[1])
# xx =(a[:3])
# print(xx)
# print(a.index(3))
# print(a.count("哈哈"))

'''
b =[1,2,3,4,5,6,"思考","哈哈",True,False,2.333]
print(b)
print(b[0])
b.pop(2)
print(b)
b.append("测试")
print(b)
b.insert(0,"人才")
print(b)

b.pop(5)
print(b)
'''



c= str(input("请输入“我爱你”，否则你就是猪:"))
if c == "我爱你":
    print ("我也爱你")
elif c == "你才是猪":
    print("哈哈")
else:
    print ("你是猪")

