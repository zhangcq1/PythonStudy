#-----------------------------基数排序(桶排序)--------------------------------
import random,time
start = time.time()


def RadixSort(data,):
    lst = [[] for i in range(10)]
    for i in range(len(str(max(data)))):#获取最大位数,排序次数为最大位数
        for ele in data:#依次将data数据入桶
            index = ele//10**i%10 #依次获取个,十,百,等位的数
            lst[index].append(ele)#按照特定位的数入桶
        data=[x for ele in lst for x in ele ]#将桶中数据依次取出,重新放到数据中
        lst = [[] for i in range(10)]#重置桶
    return data


if __name__ == '__main__':
    # data = [118, 229, 3121, 427, 152, 63, 79, 81, 95, 104, 116, 120, 2, 4, 6]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = RadixSort(data)
    # print(ret)
    end = time.time()
    print(end-start)
    input()
