"""
class 声明类的名字
然后类的名字开头必须大写
def __init__():  #这是固定的写法
类里面所有的方法，都必须要传一个参数
"""



class Girlfriend():
    def __init__(self):
        self.sex ="女"
        self.high ="160"
        self.weigt ="50kg"
        self.hair ="长发"
        self.age ="25岁"
    
    def caiyi(self,num):
        if num ==1:
            print("做饭")
        elif num ==2:
            print("看电视")
        else: 
            print("打游戏")
    def chuyi(self):
        print("精通蛋炒饭")
    def work(self):
        print("护士")

#类的实例化
cwx = Girlfriend()
cwx.caiyi(1)
cwx.chuyi()
cwx.work()
print(cwx.sex)