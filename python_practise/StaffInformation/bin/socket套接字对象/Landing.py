def register(username,password):
    username = input('Please input the username you want to register:').strip()
    password = input('Please input the password you want to register:').strip()
    if judgment(username,password):
        print('The user name you registered already exists\n')
    else:
        new_Data = "%s|%s" %(username,password)
        with open('F:/StaffInformation/db/usrname_password', 'a', encoding='utf-8') as f:
            f.write('\n%s' % new_Data)
def landing():
    username = input('Please input the username:').strip()
    password = input('Please input the password:').strip()
    if judgment(username, password):
        print('登录成功')
    else:
        print('用户名或密码不正确')

def judgment(username,password):
    with open('F:/StaffInformation/db/usrname_password','r',encoding='utf-8') as f:
        for line in f:
            line_lst = line.strip().split('|')
            if username == line_lst[0] and password == line_lst[1]:
                return True
        return False