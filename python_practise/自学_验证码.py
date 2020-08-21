import random
num1=random.randint(1,9)
num2=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz')
num3=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz')
num4=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz')
num1=str(num1)
num=num1+num2+num3+num4
print(num)
put=input('请输入验证码：')
if put==num:
    print('验证通过')
else:
    print('验证失败')
input('按任意键返回')
