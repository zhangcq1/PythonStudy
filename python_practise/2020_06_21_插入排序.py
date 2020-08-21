#-----------------------------插入排序--------------------------------
import random,time
start = time.time()
def InsertSort(data, reverse=False):
    if not reverse:
        for i in range(1, len(data)):  # 将第一个元素看成有序列表,剩余的看成待排列表
            insert_value = data[i]  # 获取到待插入的数据
            index = i - 1  # 获取到有序列表最后一个元素位置
            if insert_value < data[index]:
                while index >= 0 and insert_value < data[index]:  # 依次查找插入位置
                    data[index + 1] = data[index]  # 如果满足条件说名没找到插入位置,其余的元素向后移动一位
                    index -= 1  # 比较前一个
                data[index + 1] = insert_value  # 如果不满足条件,说明上一个位置即合适位置
        return data
    else:
        for i in range(1, len(data)):  # 将第一个元素看成有序列表,剩余的看成待排列表
            insert_value = data[i]  # 获取到待插入的数据
            index = i - 1  # 获取到有序列表最后一个元素位置
            if insert_value > data[index]:
                while index >= 0 and insert_value > data[index]:  # 依次查找插入位置
                    data[index + 1] = data[index]  # 如果满足条件说名没找到插入位置,其余的元素向后移动一位
                    index -= 1  # 比较前一个
                data[index + 1] = insert_value  # 如果不满足条件,说明上一个位置即合适位置
        return data
if __name__ == '__main__':
    # data = [8,9,1,7,2,3,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = InsertSort(data, )
    # print(ret)
    end = time.time()
    print(end-start)
    
    input()
