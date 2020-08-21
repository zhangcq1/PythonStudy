import os
def Open(local,n):
    files=os.listdir(local)#查看当前目录文件
    for file in files:#获取到每一个文件
        f_local=os.path.join(local,file)#获取新的文件路径
        if os.path.isdir(f_local):#判断f_local是否是文件夹
            print('\t'*n,file)
            Open(f_local,n+1)
        else:
            print('\t'*n,file)
Open('D:/A个人文档',1)
