import socket
def register():
    #注册要发送的请求
    username_password = input('Please input the username and password you want to register:').strip()
    username_password='1|'+username_password
    return username_password.encode('utf8')
def landing():
    #登录要发送的请求
    username_password = input('Please input the username and password:').strip()
    username_password = '2|' + username_password
    return username_password.encode('utf8')
def close():
    #断开要发送的请求
    return '3|连接断开'.encode('utf8')

client = socket.socket()
client.connect(("127.0.0.1",8899))
data1 = client.recv(1024)
while 1:
    #发送数据,并在客户端执行对应的操作
    #输入退出请求则断开连接,跳出循环
    while 1:
        #连接成功后展示主页面,然后输入对应操作
        #输入对应操作正确后方可跳出循环执行对应操作
        data = input('%s'%data1.decode('utf8')).encode('utf8')
        client.send(data)
        data2 = client.recv(1024).decode('utf8')
        data2_list = data2.strip().split('|')
        print(data2_list[1])
        if not data2_list[0] == '0':
            break
        else:
            continue
    cmd = {'1':register,\
           '2':landing,
           '3':close}
    client.send(cmd[data2_list[0]]())

    print(client.recv(1024).decode('utf8'))
    if data2_list[0] == '3':
        break


