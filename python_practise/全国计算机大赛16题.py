N=int(input('请输入数组元素个数N(N<10000):'))#输入说明:第一行是整数N(N<10000 )
x=input('请输入数组元素:')#输入数组中的N个元素
xlist=x.split(' ')#将输入数组元素转为列表
s=0#判断有无满足条件的元素
for i in range(N):#遍历列表，将列表'str'格式转换为'int'格式
    xlist[i]=int(xlist[i])
if N==len(xlist):#判断输入元素个数是否有误
    for i in range(N):#输出数组序列中6的倍数,若有多个满足条件的元素,用空格隔开
        if xlist[i]%6==0:
            print(xlist[i],end=' ')
            s+=1
    if s==0:#没有符合条件的元素则输出-1
        print('-1')
else:
    print('输入数组元素个数与设定不符')
