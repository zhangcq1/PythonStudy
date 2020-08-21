import socket
import subprocess #使用cmd命令的模块
import struct #压缩包的模块,将整形数字压缩成4个字节
#ret=struct.pack("i",1211)#i为整数模式,最小-2147483648,最大压缩2147483647,压缩后为4个字节

ssh_Server = socket.socket()
ssh_Server.bind(('127.0.0.1',8000))
ssh_Server.listen(5)
while 1:
    print('等待连接')
    conn,addr = ssh_Server.accept()
    print('连接成功')
    while 1:
        try:
            cmd = conn.recv(1024).decode('gbk') #接受客户端输入的字符串形式的cmd命令
            #在服务器端实现字符串形式的cmd命令,并获取到结果,stderr为错误命令结果,stdout为正确命令结果
            ret = subprocess.Popen(cmd,
                                   shell = True,
                                   stderr = subprocess.PIPE,
                                   stdout = subprocess.PIPE,
                                    )
            err = ret.stderr.read()#获取错误命令结果的字节,(windows默认gbk编码)
            out = ret.stdout.read()#获取正确命令结果的字节


            if err:#如果错误名存在值,说明客户端输入的是错误的cmd命令,则返回错误信息
                print(len(err))#显示错误信息字节长度
                len_err = struct.pack("i", len(err))#将错误信息字节长度压缩成4个字节
                conn.send(len_err)#发给客户端要接受的数据长度,方便客户端接受数据
                conn.send(err)#发给客户端提示错误的数据信息
            else:
                print(len(out))#显示正确信息字节长度
                len_out = struct.pack("i", len(out))#将正确信息字节长度压缩成4个字节
                conn.send(len_out)
                conn.send(out)#发给客户端提示错误的数据信息
        except Exception as e:
            print('连接已断开')
            break
