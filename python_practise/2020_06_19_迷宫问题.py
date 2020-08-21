#-----------------------------迷宫问题--------------------------------
def GetMap(row, column):  # 制作地图
    Map = []
    for i in range(row):
        Map.append([0] * column)
    for i in range(column):
        Map[0][i] = 1
        Map[row - 1][i] = 1
    for j in range(row):
        Map[j][0] = 1
        Map[j][column - 1] = 1
    return Map


def SetWall():  # 设置墙
    Map[1][2] = 1
    for i in range(7):
        Map[3][i] = 1
    Map[3][3] = 0


def ShowMap(Map):  # 显示地图
    for ele in Map:
        print(' '.join([str(i) for i in ele]))


def GetResult(x, y):  # 找路
    if Map[6][5] == 2:  # 如果终点,如果终点的值为2,说明找到路了
        return True
    else:  # 否则找路
        if Map[x][y] == 0:
            Map[x][y] = 2  # 假设能走的同
            if GetResult(x, y + 1):  # 向右,如果走通返回True
                return True
            elif GetResult(x + 1, y):  # 向下,如果走通返回True
                return True
            elif GetResult(x - 1, y):  # 向上,如果走通返回True
                return True
            elif GetResult(x, y - 1):  # 向左,如果走通返回True
                return True
            else:  # 如果都走不同说明是死路,返回False
                Map[x][y] = 3
                return False
        else:
            return False


if __name__ == '__main__':
    Map = GetMap(8, 7)
    SetWall()
    GetResult(1, 1)
    ShowMap(Map)
    input()
