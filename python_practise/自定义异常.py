class UserNameError(Exception):#自定义异常时需要继承Exception
    def __init__(self,Error='用户名错误'):#Error为UserNameError对应文本
        Exception.__init__(self,Error)#将UserNameError加入到Exception中

class PassWordError(Exception):
    def __init__(self,Error='密码错误'):
        Exception.__init__(self,Error)

def LogIn():
    username='Abc'
    password='13456'
    try:
        if username=='Abc' and password=='123456':
            print('登录成功')
        if username!='Abc':
            raise UserNameError#抛出异常UserNameError
        if password!='123456':
            raise PassWordError#抛出异常PassWordError

    except Exception as ele:#捕获异常
        print(ele)

