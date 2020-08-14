import pymysql
'''
导入pymysql
'''
class Db:
    def __init__(self,host,user,password,dbname):
        self.host=host
        self.user=user
        self.password=password
        self.db=dbname

    def chaxun(self,sql):
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db)
        cursor = db.cursor()  #获取游标
        try:
            cursor.execute(sql)
            res =cursor.fetchall()
            return res
        except:
            return "sql语句写错了"

# sql =Db("111.229.214.158","root","123456","ZXF")
# a =sql.chaxun("select * from t_admin;")
# # for i in a:
# print(a)