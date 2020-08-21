import requests
import re
import threading
import os
import time
import pymysql

# conn = pymysql.connect(
#     host='127.0.0.1',
#     user='root',
#     password='root',
#     database='mydatabase',
#     charset='utf8')
# cursor = conn.cursor()
# my = SQL()
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


class MyBaby(object):
    def __init__(self,):#address为了简洁只支持盘符
        self.url1_list=[]#存放主页面url连接
        self.url2_list=[]#存放组图资源url连接

    def Geturl_1(self,):
        '''
        获取到所有的页面链接，
        无返回值，结果直接存在self.url1_list
        '''
        start_time = time.clock()
        try:
            for i in range(2, 10):#2,160
                url = 'https://004647.com/list-14-%s.html' % i
                self.url1_list.append(url)
        except:
            pass

    def Geturl_2(self,size):
        try:
            def func2():
                '''
                1.解析主页面连接，获得组图资源连接
                2.无返回值，结果直接存在self.url2_list
                3.这里封装成函数，是因为数据请求是，I/O操作，
                    通过多线程可以提高效率
                '''
                while self.url1_list:
                    url = self.url1_list.pop()#为了避免重复，采用pop
                    size_new = len(self.url1_list)
                    html=self.GetHtml(url)#获取源码，解析，获取相关数据
                    re_url = '<ul class="detail-list">.+?</ul></div></div>'
                    ret = re.findall(re_url, html, re.S)
                    res = re.findall("https://.+?/article.+?.html", ret[0])
                    res = set(res)
                    for ele in res:#将获取到的数据写入到url2_list中
                        self.url2_list.append(ele)
            start_time = time.clock()
            for i in range(6):
                #根据电脑CPU核数获得最优线程数，这里采用了核数*2+2
                t2 = threading.Thread(target=func2)
                t2.start()
            t2.join()
        except:
            t2 = threading.Thread(target=func2)
            t2.start()

    def GetHtml(self, url):
        '''
        获取源码的封装
        :param url: 传入url链接
        :return: 返回该连接对应源码
        '''
        try:#处理异常
            address = {'user-agent': 'Mozilla/5.0'}#虚拟请求地址，有的网站会检查是否浏览器浏览
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
            html = r.text#获取到源码
            return html
        except:
            pass

    def Download(self,):
        '''
        下载逻辑代码存放
        :无返回值，直接存放对应位置
        '''
        try:
            def save():
                try:
                    while self.url2_list:
                        try:
                            my = SQL()
                            url=self.url2_list.pop()#依次取，避免重复
                            html = self.GetHtml(url)#获取源码
                            ret = re.findall('<h1>(?P<name>.+?)<span> (?P<num>.+?)</span></h1>', html, re.S)
                            res = re.findall('\d+', ret[0][1], re.S)
                            N = int(res[1])
                            # file_name=ret[0][0]#获取组图名
                            print(N)
                            for i in range(2, N):
                                #拼接组图中每张图片链接
                                str1 = '%s%s.html' % ('-', str(i))
                                new_url = url.replace('.html', str1)
                                new_html = self.GetHtml(new_url)#获取到图片链接
                                data_url = re.findall('https://img.+?gif', new_html, re.S)
                                print(data_url[0])
                                # sql = "select * from img_urls where btitle=%s"
                                # if cursor.execute(sql, data_url[0]):
                                #     print('已存在')
                                # else:
                                #     sql = "insert into img_urls(btitle) values(%s)"
                                #     cursor.execute(sql, data_url[0])
                                # conn.commit()
                                if my.isexist(data_url[0]):
                                    print('已存在')
                                else:
                                    my.save(data_url[0])
                                    print('已存在',data_url[0])
                                    my.end()
                        except:
                            pass

                    # my.end()
                except:
                    t3 = threading.Thread(target=save, )
                    t3.start()
            for i in range(6):
                t3= threading.Thread(target=save,)
                t3.start()
            t3.join()
        except:
            pass
    def run(self):
        '''
        主程序
        '''
        self.Geturl_1()
        base_url1_size = len(self.url1_list)
        self.Geturl_2(base_url1_size)
        self.Download()
baby = MyBaby()
baby.run()
