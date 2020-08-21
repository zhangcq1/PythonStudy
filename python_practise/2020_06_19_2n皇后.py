#----------------------------2n皇后问题--------------------------------
import time
start = time.time()
def GetMap(Max):#获取棋盘
    Map = []
    for i in range(Max):
        Map.append([0]*8)
    return Map

def ShowMap(Map,):#展示棋盘并返回
    ret = []
    for ele in Map:
        ret.append((ele.index(1)+1,ele.index(2)+1))
        #压缩棋盘,ret列表中的第几个元素表示第几行,对应的元组中的第一个表示白皇后放在第几列
        #对应的元组中的第二个表示黑皇后放在第几列
    return ret

def Rule(Map,row,rule):#放置的规则,如果可以放返回True,如果不可以放返回False
    #rule,传入皇后类型,白皇后为1,黑皇后为2
    i2 = row
    j2 = Map[row].index(rule)
    for i1 in range(row):
        j1 = Map[i1].index(rule)
        if j1 == j2 or abs(i2-i1)==abs(j2-j1):#如果在之前的棋子的同一列,或者对角线
            return False#说明不能放,返回False
    return True#否则返回True,能放

def GetResult(Map,row,res=[]):
    '''
    :param Map: 棋盘
    :param row: 行
    :param res: 统计所有拜访位置
    :return res :返回结果
    '''
    if row == Max:#如果row(行)==Max,说明找到了一个摆放位置
        Map = ShowMap(Map,)
        res.append(Map)
        return True
    else:
        for column1 in range(Max):
            Map[row][column1] = 1 #先让第row行第column1列元素为1,表示放置一个白皇后
            if Rule(Map,row,1):#如果该棋子满足要求
                for column2 in range(Max):#开始放黑皇后
                    if Map[row][column2] == 0:#如果该位置能放
                        Map[row][column2] = 2#先让第row行第column2列元素为2,表示放置一个黑皇后
                        if Rule(Map, row, 2):#如果该棋子满足要求
                            GetResult(Map, row + 1)#开始下一行棋子放置
                            Map[row][column2] = 0 #回溯时,重置黑皇后,获得白皇后不变,黑皇后变化所有放法
                        else:
                            Map[row][column2] = 0#如果该棋子不满足要求,重置黑皇后
                Map[row][column1] = 0 #回溯时,重置白皇后,再次获得黑皇后变化所有放法
            else:
                Map[row][column1] = 0#如果不能放,重置白皇后
    return res

if __name__ == '__main__':
    Max = 8 #棋盘大小,4*4
    Map = GetMap(Max) #获取棋盘
    res = GetResult(Map,0) #获取结果
    print('共有:%s种方法'%len(res))
#    for ret in res:
#        print(str(ret))
    end = time.time()
    print(end-start)
    input()
    
