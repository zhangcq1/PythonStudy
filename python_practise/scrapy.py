import requests
import re
import threading
import os
import time
class MyBaby(object):
    def __init__(self):
        self.url1_list=[]
        self.url2_list=[]
        self.Geturl_1()
        self.More1()
        self.More2()
    def More1(self,):
        threads=[]
        t1=threading.Thread(target=self.Geturl_2())
        t2 = threading.Thread(target=self.Geturl_2())
        t3 = threading.Thread(target=self.Geturl_2())
        t4 = threading.Thread(target=self.Geturl_2())
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        threads.append(t4)
        for ele in threads:
            ele.setDaemon(False)
            ele.start()

    def More2(self,):
        threads2=[]
        t5 = threading.Thread(target=self.Download)
        t6 = threading.Thread(target=self.Download)
        t7 = threading.Thread(target=self.Download)
        t8 = threading.Thread(target=self.Download)
        threads2.append(t5)
        threads2.append(t6)
        threads2.append(t7)
        threads2.append(t8)
        for ele in threads2:
            ele.setDaemon(False)
            ele.start()
    def Geturl_1(self, ):
        try:
            for i in range(2, 10):
                url = 'https://004647.com/list-14-%s.html' % i
                self.url1_list.append(url)
        except:
            pass
    def Geturl_2(self, ):
        try:
            while self.url1_list:
                url=self.url1_list.pop()
                html=self.GetHtml(url)
                re_url = '<ul class="detail-list">.+?</ul></div></div>'
                ret = re.findall(re_url, html, re.S)
                res = re.findall("https://.+?/article.+?.html", ret[0])
                res = set(res)
                for ele in res:
                    self.url2_list.append(ele)
        except:
            pass
    def GetHtml(self, url):
        try:
            address = {'user-agent': 'Mozilla/5.0'}
            r = requests.get(url)
            r.encoding = r.apparent_encoding
            r.raise_for_status()
            html = r.text
            return html
        except:
            pass

    def Download(self):
        time.sleep(1)
        try:
            while self.url2_list:
                url=self.url2_list.pop()
                html = self.GetHtml(url)
                ret = re.findall('<h1>(?P<name>.+?)<span> (?P<num>.+?)</span></h1>', html, re.S)
                res = re.findall('\d+', ret[0][1], re.S)
                file_name=ret[0][0]
                N=int(res[1])
                if os.path.isdir('F:/爬虫照片/'):
                    pass
                else:
                    os.mkdir('F:/爬虫照片/')
                file_path = os.path.join('F:/爬虫照片/', file_name)
                if os.path.isdir(file_path):
                    print('%s组图已存在'%file_path)
                    pass
                else:
                    os.mkdir(file_path)
                for i in range(2, N):
                    str1 = '%s%s.html' % ('-', str(i))
                    new_url = url.replace('.html', str1)
                    Picture_path=os.path.join(file_path, str(i)+'.gif')
                    if os.path.isfile(Picture_path):
                        print('%s图片已存在'% file_name+str(i)+'.gif')
                        continue
                    else:
                        new_html= self.GetHtml(new_url)
                        data_url = re.findall('https://img.+?gif', new_html, re.S)
                        data=requests.get(data_url[0])
                        print('正在下载%s'% file_name+str(i)+'.gif')
                        with open(Picture_path,'wb') as f:
                            f.write(data.content)
                        print('下载完成')
        except:
            pass
baby = MyBaby()

