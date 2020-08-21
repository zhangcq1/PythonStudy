import requests#导入requests库
import re

def GetHtml(url):
    try:
        RequestAddrss={'user-agent':'Mozilla/5.0'}#更改请求地址为Mozilla/5.0
        r=requests.get(url,headers = RequestAddrss)#获取网页源码
        r.raise_for_status()#捕获异常
        r.encoding=r.apparent_encoding#更换编码集
        return r.text#获得字符串形式网页源码
    except:
        return '请求错误'

def GetRank(Html):
    data_re=' <em class="">(?P<rank>.+?)</em>.+?<span class="title">(?P<title>.+?)</span>.+?\
    <span class="rating_num" property="v:average">(?P<score>.+?)</span>.+?\
    <span>(?P<count>.+?)评价</span>'
    data=re.compile(data_re,re.S)#re.S模式为.匹配所有字符
    return data.finditer(Html)

def Save(rank):
    for ele in rank:
        rank=ele.group('rank')
        name=ele.group('title')
        score=ele.group('score')
        number=ele.group('count')
        data_list=[{'rank':rank},{'name':name},{'score':score},{'number':number}]
        with open('Movie_rankings.txt','a',encoding='utf-8') as f:
            f.write('\n'+str(data_list))

def main():
    N=0
    for i in range(10):
        url='https://movie.douban.com/top250?start=%s&filter='%N
        Html=GetHtml(url)
        rank=GetRank(Html)
        Save(rank)
        N=N+25
        
main()
