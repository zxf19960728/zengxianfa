"""
class 声明类的名字
然后类的名字开头必须大写
def __init__():  #这是固定的写法
类里面所有的方法，都必须要传一个参数
"""



class Girlfriend():
    def __init__(self,sex,high,weigt,hair,age):
        self.sex =sex
        self.high =high
        self.weigt =weigt
        self.hair =high
        self.age =age
    
    def caiyi(self,num):
        print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weigt+"发型"+self.hair+"年龄"+self.age+"的女朋友会")
        if num ==1:
            print("做饭")
        elif num ==2:
            print("看电视")
        else: 
            print("打游戏")
    def chuyi(self):
        print("你的性别为"+self.sex+"身高"+self.high+"体重"+self.weigt+"发型"+self.hair+"年龄"+self.age+"的女朋友会")
        print("精通蛋炒饭")
    def work(self):
        print("她的职业是:")
        print("护士")

# #类的实例化
# cwx = Girlfriend("女","160cm","50kg","长发","25")
# cwx.caiyi(1)
# cwx.chuyi()
# cwx.work()


class Nvpenyou(Girlfriend):
    pass
    # def work(self):
    #     print("打针")


lisi =Nvpenyou("男","178","90","短发","26")
lisi.chuyi()
lisi.work()