import os
def Execute(path):
    if os.path.isfile(path) and path.endswith('.py'):#如果是.py直接执行
        os.system('python %s'% path)
    elif os.path.isdir:#如果是文件夹,寻找文件夹中的.py然后执行
        for name in os.listdir(path):
            new_path=os.path.join(path,name)
            os.system('python %s'% new_path)
    
Execute('C:/Users/Administrator/Desktop/A-Python')
