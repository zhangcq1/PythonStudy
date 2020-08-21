import random
def Captcha(N=4,letter=True):#默认4位验证码,且包含字母
    ret=''
    for i in range(N):#获取足够的验证位数
        res=str(random.randint(0,9))#获取数字
        if letter:#判断验证码是否需要字母
            res1=chr(random.randint(97,122))#获取小写字母
            res2=chr(random.randint(65,90))#获取大写字母
            res=random.choice([res,res1,res2])#随机抽取每一位验证码具体元素
        ret=ret+res
    return ret#返回生成验证码

print(Captcha())#获取四位带字母验证码
print(Captcha(6))#获取六位带字母验证码
print(Captcha(6,letter=False))#获取六位纯数字验证码
