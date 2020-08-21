import time
start=time.clock()
x=input('请输入M(M>N):')
xlist=x.split(' ')
for i in range(len(xlist)):
    xlist[i]=int(xlist[i])
    N=xlist[0]
    M=xlist[1]
for j in range(N,M+1):
    t=j
    s=0
    j=list(str(j))
    for k in range(len(j)):
        j[k]=int(j[k])
        s=s+j[k]**2
        #print('s的值：',s)
        #print('t的值：',t)
    if s>=t:
        print(t,end=' ')
end=time.clock()
print('运行时间：%s s'%(end-start))
