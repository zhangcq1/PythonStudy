import requests
kv = {'wd':'Python'}#关键词
kw = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
      }
r = requests.get("http://www.baidu.com/s",params = kv,headers = kw)#使用header命令模仿浏览器向百度服务器发出请求
print(r.status_code)
print(r.request.url)
