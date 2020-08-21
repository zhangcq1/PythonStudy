'''
对于整数区间[N，M]，已知:

输入说明：两个整数N和M。

输出说明：顺序输出元素数位上各个数字的平方和大于元素本身的数。

输入样例：21 25

输出样例：25

说明：例如22的数位数字为2，2，这两个数字的平方和为8，小于22，
不满足筛选条件所以不输出；25的数位数字为2，5，这两个数字平方和为29，
大于25，满足筛选条件，所以将25输出。


'''
def main():
    N,M=input('输入M和N:').split(' ')
    if int(M)<int(N):#如果用户输N,M范围不合要求,进行调整
        S=M
        M=N
        N=S
    for num in range(int(N),int(M)+1):#遍历N到M的所有数值
        result=0#收集元素数位上各个数字的平方和
        for i in str(num):
            result=result+int(i)**2
        if result>int(num):#判断是否大于元素本身的数,如果是输出
            print(num)
        
        
main()
