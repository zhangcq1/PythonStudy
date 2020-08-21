'''
资源限制
时间限制：1.0s   内存限制：256.0MB
问题描述
对于长度为5位的一个01串，每一位都可能是0或1，一共有32种可能。它们的前几个是：
00000
00001
00010
00011
00100
请按从小到大的顺序输出这32种01串。

输入格式
本试题没有输入。
输出格式
输出32行，按从小到大的顺序每行一个长度为5的01串。
样例输出
00000
00001
00010
00011
<以下部分省略>

'''
import random
def main1():
    set1=set()
    while len(set1)<32:
        c1=random.choice('01')
        c2=random.choice('01')
        c3=random.choice('01')
        c4=random.choice('01')
        c5=random.choice('01')
        c=c1+c2+c3+c4+c5
        set1.add(c)
    lst=list(set1)
    lst.sort()
    for i in lst:
        print(i)


def main2():
    lst1=[]
    num1=int('0b100000',2)
    num2=int('0b111111',2)
    for i in range(num1,num2+1):
        lst2=bin(i).split('0b1')
        lst2.remove('')
        lst1=lst1+lst2
    lst1.sort()
    for i in lst1:
        print(i)


def main3():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        print(str(a)+str(b)+str(c)+str(d)+str(e))
        




    
