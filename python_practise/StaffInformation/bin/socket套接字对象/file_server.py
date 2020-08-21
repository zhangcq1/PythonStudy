import socketserver
import struct
import os,time
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        len_name = self.request.recv(4) #接收文件名长度数据,打包后的长度,防止黏包
        name_data = struct.unpack('i', len_name)[0] #解析长度,转为int型
        file_name = self.request.recv(name_data).decode('utf8')#获取到文件名
        len_data = self.request.recv(4) #接受打包后的文件长度数据
        len_num = struct.unpack('i', len_data)[0]#解析长度,转为int型
        if os.path.isfile(file_name):#判断文件是否存在,如果存在获取文件大小
            len_size = os.path.getsize(file_name)
        else:
            len_size = 0 #如果没有,说明该文件大小为0,需要完整接受
        len_num = len_num - len_size #重新赋值待接受数据长度
        print(len_size)
        if len_num == 0:#如果待接受文件长度为0,说明文件以接受完毕
            print('文件已存在')
        else:#如果不为0,则需要先接受已经接受到的文件长度,然后将接受剩下的数据继续写入
            while  len_size % 1024 > 0:
                #如果长度大于1024,继续以1024接受
                data = self.request.recv(1024)
                len_size = len_size - len(data)
            self.request.recv(len_size)#接受残余的数据
            while  len_num > 0:#接收断点之后的数据,并写入文件
                data = self.request.recv(1024)
                with open(file_name,'ab') as f:
                    f.write(data)
                    #time.sleep(1)
                len_num = len_num - len(data)
            print(os.path.getsize(file_name))
server = socketserver.ThreadingTCPServer(('127.0.0.1',8096),Myserver)
server.serve_forever()