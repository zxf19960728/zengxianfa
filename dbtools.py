import pymysql

class Db:
    """
    这是用来操作数据的类
    """
    def __init__(self,host,user,password,dbname,port="3306"):
        self.host=host
        self.user=user
        self.password=password
        self.db=dbname
        self.port=port
    
    def chaxun(self,sql):
        """
        这个方法是用来查询数据库数据用的！
        """
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)# 连接数据库
        cursor =db.cursor()#获取游标
        try:
            cursor.execute(sql)#使用游标来执行sql语句
            res =cursor.fetchall()#获取所有结果
            return res
        except Exception as e:
            return "sql语句写错了！",e

    # sql ="select * from t_student;"
    # a =chaxun(sql)
    # for i in a:
    #     print(i)


    def xiugai(self,sql):
        """
        修改数据库里面的数据，包括新增，修改，删除
        """
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)# 连接数据库
        cursor =db.cursor()#获取游标
        try:
            cursor.execute(sql)#使用游标来执行sql语句
            db.commit()#提交，应用
            return True
        except Exception as e:
            return "sql语句写错了！",e


    # b= input("请输入sql修改语句：")
    # xg=xiugai(b)
    # print(xg)


    测试测试
