import pymysql
class SQL(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='mydatabase',
            charset='utf8')
        self.cursor = self.conn.cursor()
    def save(self,url):
        sql = "insert into home_test(name) values(%s)"
        self.cursor.execute(sql,url)
        self.conn.commit()
    def isexist(self,url):
        sql = "select * from home_test where name=%s"
        return self.cursor.execute(sql, url)
    def end(self):
        self.cursor.close()
        self.conn.close()

my = SQL()
url = 'http://www.beijing.gov.cn/photo/image_repository/wcm_image_1131546_additionl_type_200.jpg'
if my.isexist(url):
    print('已存在')
else:
    my.save(url)
my.end()