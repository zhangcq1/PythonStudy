'''
资源限制
时间限制：1.0s   内存限制：256.0MB
问题描述
已知一个正整数N，问从1~N中任选出三个数，他们的最小公倍数最大可以为多少。

输入格式
输入一个正整数N。

输出格式
输出一个整数，表示你找到的最小公倍数。
样例输入
9
样例输出
504
数据规模与约定
1 <= N <= 1000000。
'''
def main():
   N1=int(input())
   N2=N1-1
   N3=N1-2
   if N1%2==1:
      print(N1*N2*N3)
   
   else:
      if N1%3==0 and (N3-1)%3==0:
         print((N1-1)*(N2-1)*(N3-1))
      else: 
         print(N1*N2*(N3-1))

main()


