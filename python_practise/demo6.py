import time
start = time.clock()

class Ant(object):
    'Ant'
    class_name= 'Ant'
    
    def __init__(self,x = 0,y = 0,color = 'black'):
        '__init__'
        self.x = x
        self.y = y
        self.color=color
        self.info()
        
    def crawl(self,x,y):
        'crawl'
        print('crawl')
        self.info()

        
    def info(self):
        'info'
        print('当前位置：（%d,%d）' % (self.x,self.y))


    def attack(self):
        'attack'
        print('用嘴咬')
    

class Ant1(Ant):
    class_name= 'Ant1'

    def attack(self):
        print('用尾针')
        
    def fly(self):
        print('fly1')


class Ant2(Ant):
    class_name= 'Ant2'
    
    

class Ant3(Ant2,Ant1):
    class_name= 'Ant3'
    def fly(self):
        print('fly3')
    

ant3 = Ant3()

ant3.fly()




















end = time.clock()
print('程序运行时间：%s' %(end-start))
