'''
资源限制
时间限制：1.0s   内存限制：256.0MB
问题描述
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。　　
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
　　
下面给出了杨辉三角形的前4行：　
   1　　
  1 1　　
 1 2 1　　
1 3 3 1　　
给出n，输出它的前n行。
输入格式
输入包含一个数n。
输出格式
输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一
个空格分隔。请不要在前面输出多余的空格。
样例输入
4
样例输出
1
1 1
1 2 1
1 3 3 1
数据规模与约定
1 <= n <= 34。

'''
def main():
    n=int(input())
    lst=[[1],[1,1]]
    lst1=[]
    num=2
    while num<n:
        for i in range(len(lst[num-1])):
            if i==0:
                lst1.append(1)
            else:
                s=lst[num-1][i]+lst[num-1][i-1]
                lst1.append(s)
        lst1.append(1)
        lst=lst+[lst1]
        lst1=[]
        num=num+1
    for i in range(n):
        for j in range(len(lst[i])):
            print(lst[i][j],end=' ')
        print('')   
main()
