#-----------------------------选择排序--------------------------------
import random,time
start = time.time()
def SelectionSort(data,reverse=False):
    '''
    :param data: 需要排序数组
    :param reverse: 是否逆序
    :return: 排序完成的数组
    '''
    if not reverse:
        for i in range(len(data)):
            Min = i
            for j in range(i+1,len(data)):
                if data[Min] > data[j]:#找到最小的
                    Min = j
            data[i],data[Min] = data[Min],data[i]#交换到第L(从0开始,依次0,1,2....)位置上
        return data
    else:
        for i in range(len(data)):
            Max = i
            for j in range(i+1,len(data)):
                if data[Max] < data[j]:#找到最d大的
                    Max = j
            data[i],data[Max] = data[Max],data[i]#交换到第L(从0开始,依次0,1,2....)位置上
        return data
if __name__ == '__main__':
    # data = [8,9,1,7,2,3,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = SelectionSort(data, )
    # print(ret)
    end = time.time()
    print(end-start)
    input()
