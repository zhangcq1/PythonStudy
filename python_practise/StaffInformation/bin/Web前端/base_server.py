import socketserver
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("%s连接成功" % self.request)
        while True:
            ret = self.request.recv(8096)
            print(ret)
server = socketserver.ThreadingTCPServer(("127.0.0.1",8899),MyServer)#实例化客户端
server.serve_forever()#让客户端运行起来