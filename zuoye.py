from lixi import Db 
sql =Db("111.229.214.158","root","123456","ZXF")
a =sql.chaxun("select * from t_admin;")
for i in a:
    print(i)