lst = [
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,1,0,0,0,0,0,0,0,0,],
    [0,0,0,2,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
    [0,0,0,0,0,0,0,0,0,0,0,],
]
class Array(object):
    def __init__(self,array,data):
        self.array = array
        self.data = data
        self.zip_res = []
        self.recovery_res = []

    def zip_array(self):#压缩成稀疏数组
        self.zip_res.append([len(self.array),len(self.array[0])])
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if self.array[i][j] != self.data:
                    self.zip_res.append([i,j,self.array[i][j]])
        return self.zip_res

    def recovery_arry(self):#恢复数组
        for i in range(self.zip_res[0][0]):
            self.recovery_res.append([self.data for i in range(self.zip_res[0][1])])
        for i in range(1,len(self.zip_res)):
            print(len(self.recovery_res[0]))
            self.recovery_res[self.zip_res[i][0]][self.zip_res[i][1]] = self.zip_res[i][2]
        return self.recovery_res

array = Array(lst,0)
ret = array.zip_array()
print(ret)
res = array.recovery_arry()
print(res)
