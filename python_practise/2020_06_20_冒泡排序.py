#-----------------------------冒泡排序--------------------------------
def BubbleSort(data, reverse=False):
    '''
    :param data: 需要排序数组
    :param reverse: 是否逆序
    :return: 排序完成的数组
    '''
    N = len(data) - 1
    if not reverse:
        while N > 1:
            for i in range(N):
                if data[i] > data[i + 1]:  # 大的后移
                    data[i], data[i + 1] = data[i + 1], data[i]
            N -= 1
        return data
    else:
        while N > 1:
            for i in range(N):
                if data[i] < data[i + 1]:  # 小的的后移
                    data[i], data[i + 1] = data[i + 1], data[i]
            N -= 1
        return data
#-----------------------------冒泡排序(优化)--------------------------
import random,time
start = time.time()
def BubbleSort(data,reverse=False):
    '''
    :param data: 需要排序数组
    :param reverse: 是否逆序
    :return: 排序完成的数组
    '''
    N = len(data)-1
    if not reverse:
        while N>1:
            status = True
            for i in range(N):
                if data[i] > data[i+1]:#大的后移
                    status = False
                    data[i],data[i+1] = data[i+1],data[i]
            if status:
                return data
            N-=1
        return data
    else:
        while N>1:
            status = True
            for i in range(N):
                if data[i] < data[i+1]:#小的的后移
                    status = False
                    data[i],data[i+1] = data[i+1],data[i]
            if status:
                return data
            N-=1
        return data
    
if __name__ == '__main__':
    # data = [8,9,1,7,2,3,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = BubbleSort(data)
    # print(ret)
    end = time.time()
    print(end-start)
    input()
