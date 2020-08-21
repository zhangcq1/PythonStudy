#-----------------------------快速排序(冒泡排序优化)--------------------------------
import random,time
import random,time
start = time.time()
def QuickSort1(data,left,right,):#从小到大
    L = left  # 获取最左边坐标
    R = right  # 获取最右边坐标
    Middle = data[(L + R) // 2]  # 获取分割值,将数据分为两部分,大于Middle为一部分,小于Middle为一部分

    while L < R:  # 当左边的值不超过右边的值,说明没有遍历完所有数据,继续遍历
        while data[L] < Middle:  # 从左向右遍历,找到一个大于或者等于Middle的值
            L += 1
        while data[R] > Middle:  # 从右向左遍历,找到一个小于于或者等于Middle的值
            R -= 1
        if L >= R:  # 如果找到的是同一个,说明是Middle的值,直接退出,说明已经排好
            break
        data[L], data[R] = data[R], data[L]  # 如果不是,交换位置
        if data[L] == Middle:  # 如果此时左边值为Middle,说明左边已经排好,右边继续遍历
            R -= 1
        if data[R] == Middle:  # 如果此时右边值为Middle,说明右边已经排好,左边继续遍历
            L += 1
    if L == R:  # 如果L==R,说明同时指向middle,所以进行L += 1,R -= 1,将数据以middle分成两部分
        L += 1
        R -= 1
    if left < R:  # 分成两部分后,先进行左边递归,即当left>=R时,说明递归完毕,否则一直递归
        QuickSort1(data, left, R)
    if right > L:  # 然后进行右边递归
        QuickSort1(data, L, right)
    return data

def QuickSort2(data,left,right,):#从大到小
    L = left  # 获取最左边坐标
    R = right  # 获取最右边坐标
    Middle = data[(L + R) // 2]  # 获取分割值,将数据分为两部分,大于Middle为一部分,小于Middle为一部分
    while L < R:  # 当左边的值不超过右边的值,说明没有遍历完所有数据,继续遍历
        while data[L] > Middle:  # 从左向右遍历,找到一个小于或者等于Middle的值
            L += 1
        while data[R] < Middle:  # 从右向左遍历,找到一个大于或者等于Middle的值
            R -= 1
        if L >= R:  # 如果找到的是同一个,说明是Middle的值,直接退出,说明已经排好
            break
        data[L], data[R] = data[R], data[L]  # 如果不是,交换位置
        if data[L] == Middle:  # 如果此时左边值为Middle,说明左边已经排好,右边继续遍历
            R -= 1
        if data[R] == Middle:  # 如果此时右边值为Middle,说明右边已经排好,左边继续遍历
            L += 1
    if L == R:  # 如果L==R,说明同时指向middle,所以进行L += 1,R -= 1,将数据以middle分成两部分
        L += 1
        R -= 1
    if left < R:  # 分成两部分后,先进行左边递归,即当left>=R时,说明递归完毕,否则一直递归
        QuickSort2(data, left, R)
    if right > L:  # 然后进行右边递归
        QuickSort2(data, L, right)
    return data
def QuickSort(data,left,right,reverse = False):
    if not reverse:
        data1 = QuickSort1(data,left,right)
    else:
        data1 = QuickSort2(data, left, right)
    return data1

if __name__ == '__main__':
    # data = [8,9,1,7,2,3,9,1,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = QuickSort(data,0,len(data)-1,reverse=True)
    # print(ret)
    end = time.time()
    print(end-start)
    input()
