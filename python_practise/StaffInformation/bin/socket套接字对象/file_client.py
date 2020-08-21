import socket
import struct
client = socket.socket()
client.connect(('39.98.37.43',8096))
file_name = 'F:/StaffInformation/bin/4.png'.encode('utf-8')#要保存的文件名
with open('F:/StaffInformation/bin/1.png','rb',) as f:
    data = f.read()
    print(len(data))
    len_name = struct.pack('i', len(file_name))#打包文件名长度,防止黏包
    len_data = struct.pack('i',len(data))#打包文件长度,防止黏包
client.send(len_name)#先发送文件名长度,4个字节
client.send(file_name)#发送文件名
client.send(len_data)#再发送文件长度,4个字节
client.send(data)#发送文件
