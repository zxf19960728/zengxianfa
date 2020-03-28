# # # # 判断
# # # a =1
# # # b =2
# # # if a>b:
# # #     print("a比b大")
# # # else:
# # #     print("b大")


# """
# weight = int(input("请输入体重："))
# if weight <80:
#     print("你太瘦了")
# elif weight >80 and weight == 120:
#     print("你的身材刚刚好")
# elif weight > 120:
#     print("你太胖了")
# else:
#     print("666")
#     """
# # a =1
# # while a <20:
# #     print("666",a)
# #     a=a+2



light ={
    "红灯":30,
    "绿灯":35,
    "黄灯":3
}
for i in light:
    for j in range(light[i]):
        print(i,light[i]-j)