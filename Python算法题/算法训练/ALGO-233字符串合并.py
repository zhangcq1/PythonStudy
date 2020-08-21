'''
问题描述
　　输入两个字符串，将其合并为一个字符串后输出。
输入格式
　　输入两个字符串
输出格式
　　输出合并后的字符串
样例输入
一个满足题目要求的输入范例。
Hello

World
样例输出
HelloWorld
数据规模和约定
　　输入的字符串长度0<n<100
'''
def main():
    str1=input().strip()
    str2=input().strip()
    print(str1+str2)

main()
