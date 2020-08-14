'''
声明类：class
类的名称首字母必须大写，例如:Xcc
'''

class Xcc():
    """
    这是定义一个人的类
    """
    def __init__(self,name,age,hair,high,weight):
        self.name =name
        self.age =age
        self.hair =hair
        self.high =high
        self.weight =weight
    
    def jineng(self,num):
        '''
        技能
        '''
        # print("程旺星")
        print("我老婆:"+self.name)
        print("她今年:"+self.age)
        print("她的头发是:"+self.hair)
        print("她的身高是:"+self.high)
        print("她的体重:"+self.weight)
        print("她没事做的时候就:",end=" ")
        if num ==1:
            print("看电视")
        elif num ==2:
            print("玩手机")
        elif num ==3:
            print("吃饭睡觉")
        else:
            print("像猪一样叫")
    

a =Xcc("XCC","25岁","大波浪","160cm","50kg")
try:
    b = int(input())
    a.jineng(b)
except:
    print("请输入数字")
        
