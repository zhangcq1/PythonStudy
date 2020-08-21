'''
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　求出区间[a,b]中所有整数的质因数分解。
输入格式
　　输入两个整数a，b。
输出格式
　　每行输出一个数的分解，形如k=a1*a2*a3...(a1<=a2<=a3...，k也是从小到大的)
    (具体可看样例)
样例输入
3 10
样例输出
3=3
4=2*2
5=5
6=2*3
7=7
8=2*2*2
9=3*3
10=2*5
提示
　　先筛出所有素数，然后再分解。
数据规模和约定
　　2<=a<=b<=10000
'''
class Fun(object):
    def __init__(self):
        self.lst1=[2]#存放素数
        self.lst2=[]#临时存放分解的质因数
    def main(self):#函数主体
        a,b=map(int,input().split(' '))
        for num1 in range(2,b+1):#收集素数
            count=2
            while count<num1:
                if num1%count==0:
                    break
                count+=1           
                if count==num1:
                    self.lst1.append(num1)
                    
        for num2 in range(a,b+1):#主要输出函数
            if num2 in self.lst1:#如是素数情况下输出
                print('%s=%s'% (num2,num2))
            else:#非素数情况下输出
                self.Deal(num2)#调用Deal函数处理
                str1='*'.join(self.lst2)#将所有质因数转化成字符串方便输出
                print('%s=%s'% (num2,str1))
                self.lst2=[]#清空列表,方便处理下一个数


    def Deal(self,num=2):#处理函数,输如一个数字,获得其全部质因数
        for i in self.lst1:
            if num%i==0:
                self.lst2.append(str(i))
                s=num//i
                if s in self.lst1:
                    self.lst2.append(str(s))
                    break
                else:
                    self.Deal(s)
                    break      
fun=Fun()
fun.main()
