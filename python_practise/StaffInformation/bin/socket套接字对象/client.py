import socket
Client = socket.socket()
Client.connect(('127.0.0.1',8000))  # 向服务器发送连接请求(递伞),连接成功后才继续向下走
while True:
    data = input('请输入你要发送的内容:')
    if data=='exit':
        break
    Client.send(data.encode('utf-8'))#向服务器端发送请求
    ret = Client.recv(1024)#接受服务器端反馈
    print(ret.decode('utf-8'))
#Client.close()#断开与服务器端的连接