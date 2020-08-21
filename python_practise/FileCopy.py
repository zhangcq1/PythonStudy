import os

def FileCopy(path1,path2):#传入要复制的文件路径,以及要复制到的文件夹路径
    filename=os.path.basename(path1)#获取文件名
    new_path=os.path.join(path2,filename)#组合成复制后的文件路径
    if os.path.exists(new_path):#判断是否重名
        print('已有重名文件')
    elif os.path.isfile(path1) and os.path.isdir(path2):#判断输入是否正确
        with open(path1,'rb') as f1:
            file=f1.read()
            with open(new_path,'wb') as f2:
                f2.write(file)
        print('复制成功')
            
    else:
        print('请在第一个位置传入文件路径,第二个位置传入要复制到的文件夹路径')


path1='C:/Users/Administrator/Desktop/A-Python/demo1.py'
path2='C:/Users/Administrator/Desktop'
FileCopy(path1,path2)
