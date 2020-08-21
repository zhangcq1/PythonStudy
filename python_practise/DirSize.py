import os

#Dir_size使用的是递归,由于递归深度的问题,只能用于小型计算
#Dir_Size使用的是循环,可以计算大型计算,但是由于使用列表,占用内存较大

def Dir_size(dir_path='D:/A个人文档'):#定义一个函数,设置默认路径
    Size=0#初始化大小
    if os.path.isdir(dir_path):
        #判断传入的路径是否是文件夹,如果是文件夹,则执行计算文件夹大小操作
        dirs = os.listdir(dir_path)#获取该路径下所有文件夹及文件
        for ele in dirs:
            New_path=os.path.join(dir_path,ele)#获取到新路径
            if os.path.isdir(New_path):
                #判断新路径是否为文件夹,是的话递归,且将返回的大小加到Size中
                Size=Size+Dir_size(New_path)
            if os.path.isfile(New_path):
                #判断新路径是否为文件,是的话计算大小,且将大小加到Size中
                Size=Size+os.path.getsize(New_path)
    if os.path.isfile(dir_path):
        #如果传入的路径是文件,则直接计算大小并加到Size中
        Size=Size+os.path.getsize(dir_path)
    return Size#返回大小

def Dir_Size(dir_path='D:/A个人文档'):#定义一个函数,设置默认路径
    dir_list=[]#定义一个空列表,存放文件夹的路径
    Size=0#初始化大小
    dir_list.append(dir_path)#将路径参数加入列表,处理开始
    while dir_list:#循环,直到文件夹列表为空
        dir_path=dir_list.pop()#从列表尾部取出一个路径
        dirs=os.listdir(dir_path)#获取该路径下所有文件夹及文件
        for ele in dirs:#依次处理
            new_path=os.path.join(dir_path,ele)#拼接成新路径
            if os.path.isdir(new_path):#是文件夹就加入到列表继续处理
                dir_list.append(new_path)
            if os.path.isfile(new_path):#是文件就统计大小进行累加
                Size=Size+os.path.getsize(new_path)
    return Size

print(Dir_size())
print(Dir_Size())
