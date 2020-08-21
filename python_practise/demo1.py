print('爬虫练习')
#r.status_code:请求的返回状态，如果是200表示返回成功，其他表示失败
#r.encoding:从HTTP headr中猜测的响应内容编码方式
'''r.apparent_enconding:从HTTP内容中分析的响应内容的
编码方式（备选），一般比r.encoding更加准确'''
#r.text:HTTP响应内容的字符串形式，URL对应的页面内容
#r.content:HTTP响应内容的二进制文件


import requests#导入requests第三方库

def GetHtml(url):#定义一个获取HTML文本的函数
    try:#使用try,except提示错误信息
        r=requests.get(url)
        r.raise_for_status()#
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'
    
url='http://www.baidu.com'
print(GetHtml(url))




