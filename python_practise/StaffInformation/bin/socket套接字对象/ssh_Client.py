import socket
import struct
ssh_Client = socket.socket()
ssh_Client.connect(('127.0.0.1', 8000))
while 1:
    cmd = input('请输入命令:')#输入字符串形式的cmd命令
    ssh_Client.send(cmd.encode('gbk'))#将字符串形式的命令转换成字节(Windows中cmd编码默认gbk)
    len_data1 = ssh_Client.recv(4)#先接受接下来要接受数据的具体长度
    len_data = struct.unpack("i",len_data1)[0]#解压后获取int型数据的具体长度
    print(len_data)#输出接下来要接受的数据长度
    len_res = 0#初始化接受数据总长
    res=b""#初始化接受的数据(字节)
    while len_res < len_data:#判断已经获取的总长是否小于数据总长,如果小于继续获取
        data = ssh_Client.recv(1024)#每次接受1024字节数据
        res = res + data#将数据累加到总的数据中
        len_res = len_res + len(data)#将已经获取的数据长度累加
    print(res.decode('gbk'))#将获取的数据解码输出



