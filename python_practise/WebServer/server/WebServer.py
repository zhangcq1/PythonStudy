import socketserver
from server.readfile import ReadFile
index_file = ReadFile('../html/index.html')

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
            try:
                len_name = self.request.recv(1024)  # 接收文件名长度数据,打包后的长度,防止黏包
                # print(len_name)
                self.request.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
                self.request.sendall(index_file.read_file())
                len_name = self.request.recv(1024)  # 接收文件名长度数据,打包后的长度,防止黏包
                print(len_name)
                # self.request
            except:  # 意外掉线
                self.remove()

    def finish(self):
        pass
        # print("清除了客户端%s。" %self)
    def remove(self):
        print("客户端掉线了%s。" %self)


server = socketserver.ThreadingTCPServer(('127.0.0.1',8096),Myserver)
server.serve_forever()