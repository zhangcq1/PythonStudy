#-----------------------------线性查找算法--------------------------------

import random,time
start = time.time()
def find(data,keyword):
    res = []
    for i in range(len(data)):
        if data[i] == keyword:
            res.append(i)
    return res
if __name__ == '__main__':
    # data = [118, 229, 3121, 427, 152, 63, 79, 81, 95, 104, 116, 120, 2, 4, 6]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = find(data,2)
    print(ret)
    end = time.time()
    print(end-start)
    input()
