import random
def RedEnvelope(Amount,Quantity):
    #先把金额分配完毕,然后再分给具体个人
    res=[]
    for i in range(Quantity-1):
        ele=format(random.uniform(0.01,Amount),'.2f')
        res.append(ele)
        Amount=Amount-float(ele)
    res.append(format(Amount,'.2f'))
    while len(res)!=0:
        yield res.pop()
        
RedEnvelope=RedEnvelope(100,5)
for i in range(5):
    print(RedEnvelope.__next__())
