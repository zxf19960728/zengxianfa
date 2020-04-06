import time

now = time.strftime("%y-%m-%d %H:%M:%S")
print(now)
xinqing =input("请输入你要记录是事情：")
with open("D:\心情.doc","a",encoding="utf8") as a:
    a.write(now+"\n")
    a.write(xinqing+"\n")
    a.write("----------------------"+"\n")


