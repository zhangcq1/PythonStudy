#----------------------------2n皇后问题(优化)--------------------------------
import time
start = time.time()
def GetMap(Max):#获取棋盘
    Map = []
    for i in range(Max):
        Map.append([0]*Max)
    return Map
def RecoverMap(list_map):#恢复棋盘
    Map = []
    for i in range(len(list_map)):
        Map.append([0] * len(list_map))
    for i in range(len(list_map)):
        Map[i][list_map[i]-1] = 1
    return Map
def SaveMap1(Map,):#展示棋盘并返回
    ret = []
    for ele in Map:
        ret.append(ele.index(1)+1)
        #压缩棋盘,ret列表中的第几个元素表示第几行,对应的元组中的第一个表示白皇后放在第几列
        #对应的元组中的第二个表示黑皇后放在第几列
    return ret

def SaveMap2(Map,):#展示棋盘并返回
    ret = []
    for ele in Map:
        ret.append((ele.index(1)+1,ele.index(2)+1))
        #压缩棋盘,ret列表中的第几个元素表示第几行,对应的元组中的第一个表示白皇后放在第几列
        #对应的元组中的第二个表示黑皇后放在第几列
    return ret

def Rule(Map,row,queen):#放置的规则,如果可以放返回True,如果不可以放返回False
    #queen,传入皇后类型,白皇后为1,黑皇后为2
    i2 = row
    j2 = Map[row].index(queen)
    for i1 in range(row):
        j1 = Map[i1].index(queen)
        if j1 == j2 or abs(i2-i1)==abs(j2-j1):#如果在之前的棋子的同一列,或者对角线
            return False#说明不能放,返回False
    return True#否则返回True,能放

def GetResult(Map,row,queen,save,res):
    '''
    :param Map: 棋盘
    :param row: 放置第几行
    :param queen: 皇后类型
    :param save: 存储函数
    :param res: 结果(列表)
    :return: 结果res
    '''
    if row == Max:#如果row(行)==Max,说明找到了一个摆放位置
        Map = save(Map,)
        res.append(Map)
        return True
    else:
        for column1 in range(Max):
            if Map[row][column1] == 0:
                Map[row][column1] = queen #先让第row行第column1列元素为queen,表示放置一个皇后
                if Rule(Map,row,queen):#如果该棋子满足要求
                    GetResult(Map, row+1, queen, save, res)#开始下一行棋子放置
                    Map[row][column1] = 0 #回溯时,重置皇后,再次获得皇后变化所有放法
                else:
                    Map[row][column1] = 0#如果不能放,重置皇后
    return res
if __name__ == '__main__':
    Max = 8 #棋盘大小,4*4
    Map = GetMap(Max) #获取棋盘
    res1 = GetResult(Map,0,1,SaveMap1,[]) #获取白皇后放置结果
    print('白皇后共有:%s种方法'%len(res1))
    for ele in res1:#遍历获取放置白皇后的棋盘,进一步获取白皇后加黑皇后放置结果
        Map1 = RecoverMap(ele)#恢复棋盘
        res2 = GetResult(Map1,0,2,SaveMap2,[])
    print('白皇后加黑皇后共有:%s种方法' % len(res2))
    end = time.time()
    print(end-start)
    input()
