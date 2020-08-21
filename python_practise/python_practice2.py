'''
给出一个字符串（长度<10000），统计其中四个字母（b、m、p、t）出现的次数，
并按出现次数降序输出字母和该字母的出现次数（不区分大小写），
如果两个字母的出现次数一样，则按照字母升序输出。
输入说明：一个字符串。
输出说明：分4行输出，每个字母一行。格式为字母和出现次数，以单个空格分隔。
输入样例：123aabapsobwo
输出样例：b 2
p 1
m 0
t 0
'''
#方法一,使用内置函数count,直接返回字符串中某字符或者字符串的个数
def main1():
    str1=input('请输入一个字符串:')
    print('b',str1.count('b'),sep=' ')
    print('p',str1.count('p'),sep=' ')
    print('m',str1.count('m'),sep=' ')
    print('t',str1.count('t'),sep=' ')   
        
#方法二
def main2():
    str1=input('请输入一个字符串:')
    num_b,num_p,num_m,num_t=0,0,0,0#初始化b,p,m,t个数
    for i in str1:#遍历每个字符串的每个元素,并分别进行累加
        if i=='b':
            num_b=num_b+1
        if i=='p':
            num_p=num_p+1
        if i=='m':
            num_m=num_m+1
        if i=='t':
            num_t=num_t+1        
    print('b',num_b,sep=' ')
    print('p',num_p,sep=' ')
    print('m',num_m,sep=' ')
    print('t',num_t,sep=' ')
main1()
main2()
