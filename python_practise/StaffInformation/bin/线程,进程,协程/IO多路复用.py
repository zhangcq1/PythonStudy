from gevent import monkey#
monkey.patch_all()#设置遇到I/O就切换
import requests,time
import gevent

start = time.time()
def GetHtml(url):
    '''
    获取源码的封装
    :param url: 传入url链接
    :return: 返回该连接对应源码
    '''
    try:  # 处理异常
        address = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
      } #使用headers命令模仿浏览器向百度服务器发出请求
        r = requests.get(url,headers = address)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        html = r.text  # 获取到源码
        print(url,'\n',)
    except Exception as e:
        print(e)
gevent.joinall([
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=a"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=b"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=c"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=d"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=e"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=f"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=g"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=h"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=i"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=j"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=k"),
    gevent.spawn(GetHtml,"https://www.baidu.com/s?wd=l"),

])

# html1 =GetHtml("https://www.baidu.com/s?wd=a")
# html2 =GetHtml("https://www.baidu.com/s?wd=b")
# html3 =GetHtml("https://www.baidu.com/s?wd=c")
# html1 =GetHtml("https://www.baidu.com/s?wd=d")
# html2 =GetHtml("https://www.baidu.com/s?wd=e")
# html3 =GetHtml("https://www.baidu.com/s?wd=f")
# html1 =GetHtml("https://www.baidu.com/s?wd=g")
# html2 =GetHtml("https://www.baidu.com/s?wd=h")
# html3 =GetHtml("https://www.baidu.com/s?wd=i")
# html1 =GetHtml("https://www.baidu.com/s?wd=j")
# html2 =GetHtml("https://www.baidu.com/s?wd=k")
# html3 =GetHtml("https://www.baidu.com/s?wd=l")

end = time.time()
print('运行时间%.2f:' %(end-start))

#协程运行时间30.11:32.88:
#普通运行时间38.54:39.57