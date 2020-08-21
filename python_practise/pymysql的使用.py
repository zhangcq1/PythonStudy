import pymysql

username  = input("请输入用户名:")
password  = input("请输入密码:")
#建立连接
sql_conn = pymysql.connect(
    host='localhost',
    user='root',
    password="root",
    database='user_info',
    port=3306,
    charset='utf8',
)

#创建游标
cur = sql_conn.cursor()
sql = 'select * from info where username = %s and password = %s'
print(sql)
ret = cur.execute(sql,[username,password])
print(ret)

cur.close()
sql_conn.close()
if ret:
    print('登录成功')