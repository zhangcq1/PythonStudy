#coding=utf8
from urllib import request#负责打开浏览url内的html 文本
import re
import urllib,os
url='https://www.mzitu.com/page/2/'
def get_image(url): #获取页面源码
    page = urllib.request.urlopen(url)
    html = page.read() #解码，否则报错
    html = html.decode('utf8') #正则匹配获取（）的内容
    reg = r'src="(https.+?.[jpg,png])"'
    imge = re.compile(reg) # 获取正则匹配的数据，"(.+?.jpg)" 的数据，返回一个list
    imglist = imge.findall(html)
    return imglist
def save_img(imglist):
    dir = os.path.join(os.path.dirname(__file__),'img')
    i=1
    for img in imglist: #python3格式化字符串的另一种写法
        imgpath = 'C:/UserspAdministrator/Desktop/P/%d.jpg' % i
        try: #urlretrieve下载图片并保存到本地
            urllib.request.urlretrieve(img,imgpath)
            i += 1
            print(u'图片开始下载')
        except Exception:
            print(f'image:{img}下载失败')
            continue
imglist = get_image(url)
save_img(imglist)
