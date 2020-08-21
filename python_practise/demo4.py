import time
import demo5
from random import random
start= time.clock()




class Learn(object):
    "Learn help."
    def __init__(self):
        self.name = 'name: practise'
        self.date = 'date: 2020/2/9'
        self.demo5= demo5.Player()
        
    def PrintHelloWorld(self,count):
        "PrintHelloWorld help."
        i=0
        while i<=count:
            print('Number %d : Hello world' %i)
            i+=1
        else:
            print('End of execution')
            
    def ReturnList(self,number):
        i=0
        list_=[]
        while i<=number:
            list_.append(i)
            i+=1
        else:
            print('End of execution')
        return list_
    
    def AddList(self,list_):
        sum_ = 0
        for i in list_:
            sum_=sum_+i
        return sum_
    def ChangNumber(self,*change_number,a=0,b=0):
        print('change_number',change_number)
        print('change_number type:',type(change_number))
        print('a:',a)
        print('a type:',type(a))
        print('b:',b)
        print('b type:',type(b))


        
class Demo1(object):
    def __init__(self):
        self.name = 'name: demo1'
    def Add(self,a=1,b=3):
        c=a+b
        return c
    def PrintWords(self,word='Hello,Python'):
        print(word)





        
learn1=Learn()

player_date=learn1.demo5.date
player_name=learn1.demo5.name
print(player_name)
print(player_date)
print(dir(Learn))
print(Learn.__doc__)
print(help(Learn))

















end = time.clock()
Time=end-start
print('Running time: %s Seconds' %(end-start))

