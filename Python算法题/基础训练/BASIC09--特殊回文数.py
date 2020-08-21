'''
资源限制
时间限制：1.0s   内存限制：512.0MB
问题描述
　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满
    足各位数字之和等于n 。

输入格式
　　输入一行，包含一个正整数n。
输出格式
　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
样例输入
52
样例输出
899998
989989
998899
数据规模和约定
　　1<=n<=54。

'''
def main():
    n=int(input())
    lst=[]#定义空列表,储存所有5位,和6位数的回文数
    for i in range(10):#收集所有5位回文数
        for j in range(10,100):
            str1=str(j)+str(i)+str(j)[::-1]
            lst.append(int(str1))
    
    for i in range(100,1000):#收集所有6位回文数
        str2=str(i)[0]+str(i)[1]+str(i)[2]
        str3=str2+str2[::-1]
        lst.append(int(str3))
    lst.sort()#注意,这里要把列表排序,否则检测系统会返回错误
    for num in lst:#遍历回文列表,查找符合要求的回文
        num1=str(num)
        if len(num1)==5:#5位数中符合要求的回文
            res=int(num1[0])*2+int(num1[1])*2+int(num1[2])
            if res==n:
                print(num)
        else:#6位数中符合要求的回文
            res=int(num1[0])*2+int(num1[1])*2+int(num1[2])*2
            if res==n:
                print(int(num))           
main()
