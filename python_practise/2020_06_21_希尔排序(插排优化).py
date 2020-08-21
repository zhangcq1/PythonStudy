#-----------------------------希尔排序--------------------------------
import random,time
start = time.time()
def ShellSort(data,reverse = False):
    N = len(data) // 2
    # 获得分组个数,第一次分组为总数//2个,接下来依次除2取整为组数
    # 例如10个数据,分组数依次为5,2,1
    if not reverse:
        while N>0: #每次分组后都进行插入排序
            for i in range(N,len(data)):#遍历各分组的最后一个数据
                insret_data = data[i]#插入数据即为分组最后一个数据
                index = i -N #开始遍历的下标,(同组中在要插入元素之前的第一个)
                if insret_data < data[index]:#如果要插入元素比前一个元素大,不用排序否则执行排序
                    while index>=0 and insret_data < data[index]:
                        # 当并未遍历完该组所有元素,且插入元素比前一个元素小,继续寻找,否则就找到位置
                        data[index+N] = data[index] #将元素后移
                        index = index - N #切换到再前一个元素,继续比较
                    data[index+N] = insret_data #index+N 即为插入的位置
            N = N//2
        return data
    else:
        while N>0: #每次分组后都进行插入排序
            for i in range(N,len(data)):#遍历各分组的最后一个数据
                insret_data = data[i]#插入数据即为分组最后一个数据
                index = i -N #开始遍历的下标,(同组中在要插入元素之前的第一个)
                if insret_data > data[index]:#如果要插入元素比前一个元素小,不用排序,否则执行下列排序
                    while index>=0 and insret_data > data[index]:
                        # 当并未遍历完该组所有元素,且插入元素比前一个元素大,继续寻找,否则就找到位置
                        data[index+N] = data[index] #将元素后移
                        index = index - N #切换到再前一个元素,继续比较
                    data[index+N] = insret_data #index+N 即为插入的位置
            N = N//2
        return data
if __name__ == '__main__':
    # data = [8,9,1,7,2,3,5,4,6,0]
    data = [random.randint(1,10000) for i in range(10000)]
    ret = ShellSort(data, )
    # print(ret)
    end = time.time()
    print(end-start)
    input()
