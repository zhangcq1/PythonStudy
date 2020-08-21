import requests
import bs4
from bs4 import BeautifulSoup

def GetUrl(url):
    try:
        RequestAddrss={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers = RequestAddrss)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        return('请求错误')
    
def HtmlDeal(html):
    soup=BeautifulSoup(html,'html.parser')
    print(soup.a)
    print(soup.a.attrs['title'])
  




def DownLoad(r1):
    i=1
    path='C:/Users/Administrator/Desktop/P/%d.jpg'%i
    with open(path,'wb') as f:
        f.write(r1.content)
        f.close()
        i=i+1
def NewUrl:
    new_url=set()
    
def OldUrl:
    pass


def main():
    for url in old_url:
        html=GetUrl(url)
        HtmlDeal(html)
main()
