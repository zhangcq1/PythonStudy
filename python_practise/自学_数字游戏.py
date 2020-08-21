import random
num=random.randint(1,100)
end=False
count=0
# noinspection PyInterpreter
while not end:
   guess=int(input('请输入一个【0-100】的数：'))
   if guess==num:
      end=Truess
   elif guess>num:
      print('大了')
   elif guess<num:
      print('小了')
   count+=1
print('恭喜你，猜了{}次，终于猜对了！答案是{}！'.format(count,num))
