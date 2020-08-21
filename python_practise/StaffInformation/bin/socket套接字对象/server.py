import socket #导入socket模块
Server = socket.socket()#创建一个socket对象,
Server.bind(('127.0.0.1',8000))#绑定Ip和端口
Server.listen(5) #设置5个人访问
while 1:
    print('等待连接')
    conn, addr = Server.accept()  # 等待客户端连接,如果没人链接,陷入等待
    # conn为连接的介质(伞),服务器端要通过该介质(伞)进行收发数据
    # addr为客户端的地址信息
    print('连接成功')
    while 1:
        try:
            ret=conn.recv(1024)#接受数据吧(字节),一次性接受1024字节
            if ret==b'exit':
                break
            print(ret.decode('utf8'))
            conn.send('你好'.encode('utf-8'))#向客户端发送数据(字节)
        except Exception as e:
            print('断开连接')
            break
#conn.close()#断开与客户端的连接
#Server.close()#关闭服务端,停止服务

