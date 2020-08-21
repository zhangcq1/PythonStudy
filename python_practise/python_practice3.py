'''
有一个DNA序列，用字符串S表示（仅包含’A’、’C’、’G’、’T’四种字符，
长度<100000）。现有N个待检测的基因片段（序号分别是1，2...N），用字符
串Ti（i=1，2..,N）表示（仅包含’A’、’C’、’G '、’T’四种字符，长度<1000）。
请分别检测DNA序列S中是否存在这些基因片段，并按下面输出说明格式依次输出检测结果。

输入说明：第一行是DNA序列S。
第二行是正整数N，表明有N个待检测的基因片段，之后有N行，分别表示这N个待检测的
基因片段，即每行一个基因片段。
输出说明：依次匹配这N个待检测的基因片段，如果DNA序列S中存在第i个待检测的基因
片段，输出Ti：ALERT所在位置（即Ti的首字母在S中的位置，如果出现多次，输出第
一次出现的位置，S的起始位置为1）；如果不存在则输出Ti:SAFE。
输入样例:
ATCGCGCGAATTCATCGTTCGA
3
CG
TT
CGA
输出结果:
T1 :ALERT 3
T2 :ALERT 11
T3 :ALERT 7
'''
def main():
    S=input('请输入一个DNA序列:')
    N=int(input('请输入待检测基因片段个数:'))
    T={}
    for i in range(1,N+1):
        T1="T"+str(i)
        print(T1,':',end='')
        T2=input()
        T[T1]=T2
    for i in T:
        if T[i] in S:
            print(i,':ALERT',S.find(T[i])+1)
        else:
            print(i,':SAFE')
main()
