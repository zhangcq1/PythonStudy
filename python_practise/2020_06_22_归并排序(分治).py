#-----------------------------归并排序(分治)--------------------------------
import random,time
start = time.time()

def Merge1(data,left,mid,right,):#从小到大排
    '''
    传入两部分数据,然后整合到一起
    :param data: 需要排序的数据
    :param left: 需要整合数据最左边
    :param mid: 需要整合数据中间
    :param right: 需要整合数据最右边
    '''
    temp = [] #定义空数组,暂存排序好的数据
    i = left #第一部分数据下标开始位置
    j = mid+1 #第二部分数据下标开始位置

    # 当两部分数据有一部分被遍历完后退出
    while i<=mid and j<=right:

        # 比较两部分数据,从小到大依次放入到临时数组temp
        if data[i] < data[j]:
            temp.append(data[i])
            i+=1
        else:
            temp.append(data[j])
            j+=1

    #退出循环时,把两部分数据有完全遍历的数据依次追加到temp完成排序
    while i<=mid:
        temp.append(data[i])
        i += 1
    while j<=right:
        temp.append(data[j])
        j += 1

    # 将整理好的数据更新到原始数据中
    # 元素数据更新的范围为data[left,right],逐一遍历更新
    index = left
    for i in range(len(temp)):
        data[index]=temp[i]
        index+=1


def Merge2(data, left, mid, right, ):  # 从大到小排
    '''
    传入两部分数据,然后整合到一起
    :param data: 需要排序的数据
    :param left: 需要整合数据最左边
    :param mid: 需要整合数据中间
    :param right: 需要整合数据最右边
    '''
    temp = []  # 定义空数组,暂存排序好的数据
    i = left  # 第一部分数据下标开始位置
    j = mid + 1  # 第二部分数据下标开始位置

    # 当两部分数据有一部分被遍历完后退出
    while i <= mid and j <= right:

        # 比较两部分数据,从大到小依次放入到临时数组temp
        if data[i] > data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1

    # 退出循环时,把两部分数据有完全遍历的数据依次追加到temp完成排序
    while i <= mid:
        temp.append(data[i])
        i += 1
    while j <= right:
        temp.append(data[j])
        j += 1

    # 将整理好的数据更新到原始数据中
    # 元素数据更新的范围为data[left,right],逐一遍历更新
    index = left
    for i in range(len(temp)):
        data[index] = temp[i]
        index += 1


def MergeSort(data,left,right,reverse = False):
    if left < right:
        mid = (left+right)//2
        MergeSort(data,left,mid,reverse)
        MergeSort(data, mid+1, right,reverse)
        if not reverse:
            Merge1(data,left,mid,right)
        else:
            Merge2(data, left, mid, right)
    return data


if __name__ == '__main__':
    # data = [8,9,1,7,2,3,9,1,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = MergeSort(data,0,len(data)-1)
    # print(ret)
    end = time.time()
    print(end-start)
    input()
