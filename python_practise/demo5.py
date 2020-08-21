import random

class Player(object):
    
    def __init__(self):
        self.name = Player
        self.date = 'date: 2020/2/10'

    def Changdict(self,a,b=0,**adct):
        print('a:',a)
        print('b:',b)
        print('adct:',adct)
    def Cube(self,name,**nature):
        all_nature = {'x':1,'y':1,'z':1,'color':'white','weight':1}
        all_nature.update(nature)
        print(name,'立方体的属性：')
        print('体积：',all_nature['x']*all_nature['y']*all_nature['z'])
        print('颜色：',all_nature['color'])
        print('重量：',all_nature['weight'])
    def Mysum(self,a,b):
        return a+b
    def Change(self,aint,alst):
        aint=0
        alst[0]=0
        alst.append(4)
        print('aint:',aint)
        print('alst:',alst)
    def Myfun1(self,lst=set()):
        num=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghxyz')
        lst.add(num)
        print(lst)
    def Myfun2(self):
        global a
        a=0
        a+=3
        print('函数内部a：',a)
class DemoInit(object):
    
    def __init__(self,x,y=12):
        self.x=x
        self.y=y

        
    def myadd(self):
        return self.x+self.y

def coord_chng(x,y):
    return (abs(x),abs(y))


class Ant:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.disp_point()

        
    def move(self,x,y):
        
        self.edit_point(x,y)
        self.disp_point()


    def edit_point(self,x,y):
        self.x+=x
        self.y+=y


    def disp_point(self):
        print('当前位置：(%d,%d)' %(self.x,self.y))
        
        

