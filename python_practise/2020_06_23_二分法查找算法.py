#-----------------------------二分法查找--------------------------------
import random,time
start = time.time()

def find(data,keyword,left,right):
    '''
    二分法查找
    :param data: 有序数组
    :param keyword: 要查找的数据
    :param left: 数组左索引
    :param right: 数组右索引
    :return: 所有符合条件下标
    '''
    middle = (left+right)//2
    if left>right:#当左边的数大于右边说明遍历完毕
        return -1
    if  keyword < data[middle]:#如果要查的值比中间值小,向左递归
        return find(data,keyword,left,middle-1)
    elif keyword > data[middle]:#如果要查的值比中间值大,向右递归
        return find(data, keyword, middle+1, right)
    else:
        L = middle-1
        while keyword==data[L]:#找到左边所有符合值
            L-=1
        R = middle + 1
        while keyword == data[R]:#找到右边所有符合值
            R += 1
        return [x for x in range(L+1,R)]#将所有符合值加入到列表并返回


if __name__ == '__main__':
    # data = [2, 4, 6, 63, 79, 81,95, 95,95,95, 104, 116, 118, 120, 152, 229, 427, 3121]
    data = [random.randint(1,10000) for i in range(10000)]
    data.sort()
    ret = find(data,95,0,len(data))
    print(ret)
    end = time.time()
    print(end-start)
    input()
