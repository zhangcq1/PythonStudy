import requests
import re
import threading
import os
import time

class MyBaby(object):
    def __init__(self,):#address为了简洁只支持盘符
        self.url_list=[]#存放页面url连接
    def Geturl_1(self,):
        '''
        获取到所有的页面链接，
        无返回值，结果直接存在self.url1_list
        '''
        url = 'https://top.cardbaobao.com/gouwu.shtml'
        html = self.GetHtml(url)
        re_1 = '<h3>.+?</h3>'
        res = re.findall(re_1,html,re.S)
        re_2 = "www.+?shtml"
        re_3 = 'title.+?"(?P<nA>.+?)"'
        for ele in res:
            ret1 = re.findall(re_2, ele, re.S)
            ret2 = re.search(re_3, ele, re.S)
            dic = {ret2.group('nA'):'https://'+ret1[0]}
            self.url_list.append(dic)
    def Geturl_2(self):
        try:
            re_1 = '<li><div.+?</span>(?P<aa>.+?)</div></li>.+?提现额度:</span>(?P<ab>.+?)</div></li>.+?免息期:</span>(?P<ac>.+?)</div></li>.+?信用额度:</span>(?P<ad>.+?)</div></li>'
            i=0
            while self.url_list:
                ele = self.url_list.pop()
                i=i+1
                for key,value in ele.items():
                    name =str(i)+';'+key
                    url = value
                html = self.GetHtml(url)
                ret = re.search(re_1, html, re.S)
                nianfei = ret.group('aa')
                mianxiqi = ret.group('ac')
                edu = ret.group('ad')
                print(2)
                with open('info.txt','a',encoding='utf8') as f:
                    print(3)
                    f.write('\n\n'+name+';'+nianfei+';'+mianxiqi+';'+edu)
        except:
            print(1)

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

baby = MyBaby()
baby.Geturl_1()
baby.Geturl_2()
