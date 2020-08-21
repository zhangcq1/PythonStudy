'''
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　回文串，是一种特殊的字符串，它从左往右读和从右往左读是一样的。小龙
    龙认为回文串才是完美的。现在给你一个串，它不一定是回文的，请你计算
    最少的交换次数使得该串变成一个完美的回文串。
交换的定义是：交换两个相邻的字符
　　例如mamad
　　第一次交换 ad : mamda
　　第二次交换 md : madma
　　第三次交换 ma : madam (回文！完美！)
输入格式
　　第一行是一个整数N，表示接下来的字符串的长度(N <= 8000)
　　第二行是一个字符串，长度为N.只包含小写字母
输出格式
　　如果可能，输出最少的交换次数。
　　否则输出Impossible
样例输入
5
mamad
样例输出
3
'''
class Perfect(object):#定义一个类
    def main(self):#定义主函数
        N=int(input())
        str1=input().strip()
        if self.Judge(N,str1):#通过判断函数是否可以变成一个完美回文串
            result=self.Operation(N,str1)
            print(result)
        else:#如果不能,输出Impossible
            print('Impossible')
    def Judge(self,N,Str):#判断函数,判断是否可变成完美回文串
        Str_P='abcdefghijklmnopqrstuvwxyz'
        if N%2==0:
            for S in Str_P:
                if Str.count(S)%2==1:
                    return False
            return True
        else:
            num=0
            for S in Str_P:
                if Str.count(S)%2==1:
                    num=num+1
                    if num==2:
                        return False
            return True
    def Operation(self,N,Str):#如果可变,返回需要多少步.
        count=0
        lst=list(Str)
        for i in range(N//2):
            if lst.count(lst[0])!=1:  
                step=lst[::-1].index(lst[0])
                lst.pop(0)
                lst.pop(-(step+1))
                count=count+step
            else:
                step=len(lst)//2
                lst.pop(0)
                count=count+step
        return count
perfect=Perfect()
perfect.main()
