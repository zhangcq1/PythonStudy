#----------------------------八皇后问题--------------------------------
def GetMap(Max):#获取棋盘
    Map = []
    for i in range(Max):
        Map.append([0]*8)
    return Map

def ShowMap(Map,):#展示棋盘并返回
    ret = []
    for ele in Map:
        ret.append(ele.index(1)+1) #压缩棋盘,ret列表中的第几个元素表示第几行,对应的数表示第几列
        # print(' '.join([str(i) for i in ele]))
    return ret

def Rule(Map,row):#放置的规则,如果可以放返回True,如果不可以放返回False
    i2 = row
    j2 = Map[row].index(1)
    for i1 in range(row):
        j1 = Map[i1].index(1)
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
        for column in range(Max):
            Map[row][column] = 1 #先让第row行第column列元素为1,表示放置一个棋子
            if Rule(Map,row):#如果该棋子满足要求
                GetResult(Map,row+1)#继续防止
                Map[row][column] = 0 #此为回溯的时候,将之前棋子清空,因为同一行只能有一个棋子
            else:
                Map[row][column] = 0#如果不能放,重置该点
    return res

if __name__ == '__main__':
    Max = 8
    Map = GetMap(Max)
    res = GetResult(Map,0)
    print('共有:%s种方法'%len(res))
    for ret in res:
        print(str(ret))
    input()
