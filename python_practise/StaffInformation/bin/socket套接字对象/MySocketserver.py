import socketserver
import Page
connect_pool = []
class Mysrerver(socketserver.BaseRequestHandler):
    #实现服务端处理多用户请求需要重写socketserver.BaseRequestHandler类
    #且必须重写handle方法,该方法为主要代码逻辑
    def handle(self):
        print("%s连接成功" %self.request)
        #self.request就是之前conn,是客户端递过来的伞
        self.request.send(Page.page1.encode('utf8'))
        self.pool()#获取当前连接客户端个数
        try:
            while 1:
                #当用户完成注册或者登录操作进入相关指令操作,将注册内容写入数据库,
                # 如果登录则通过数据库判断输入内容是否输入正确
                #当用户输入退出指令断开连接
                while 1:
                    #主页面逻辑,接受到客户端的请求指令,指令正确跳出循环,否则让客户端重新输入
                    cmd1 = self.request.recv(1024).decode('utf8')
                    cmd = {'1':('1|%s'% Page.register_page ).encode('utf8'),\
                           '2':('2|%s'% Page.landing_page ).encode('utf8'),\
                           '3':('3|%s'% Page.close_page ).encode('utf8')}
                    if cmd1 in cmd.keys():
                        self.request.send(cmd[cmd1])
                        break
                    else:
                        self.request.send(('0|%s' % Page.error_page) .encode('utf8'))
                        continue
                data2 = self.request.recv(1024).decode('utf8')
                data2_list = data2.strip().split('|')
                cmd = {'1': self.register, \
                       '2': self.landing, \
                       '3': self.request.close}
                if data2_list[0] == '3':
                    cmd[data2_list[0]]()
                else:
                    username = data2_list[1]
                    password = data2_list[2]
                    self.request.send(cmd[data2_list[0]](username,password))
        except:
            connect_pool.pop()
            print('当前连接个数为%s' % len(connect_pool))
    def register(self,username, password):
        #注册代码逻辑
        if self.judgment(username, password):
            return 'The user name you registered already exists\n'.encode('utf8')
        else:
            new_Data = "%s|%s" % (username, password)
            with open('F:/StaffInformation/db/usrname_password', 'a', encoding='utf-8') as f:
                f.write('\n%s' % new_Data)

    def landing(self,username, password):
        #登录代码逻辑
        if self.judgment(username, password):
            return '登录成功'.encode('utf8')
        else:
            return '用户名或密码不正确'.encode('utf8')

    def judgment(self,username, password):
        #如果数据库存在返回True,不存在返回False,用于查看用户名是否被注册,或者登录时用户名和密码是否正确
        with open('F:/StaffInformation/db/usrname_password', 'r', encoding='utf-8') as f:
            for line in f:
                line_lst = line.strip().split('|')
                if username == line_lst[0] and password == line_lst[1]:
                    return True
            return False

    def pool(self,):
        #存放正在运行的客户端个数
        connect_pool.append(1)
        print('当前连接个数为%s' % len(connect_pool))
server = socketserver.ThreadingTCPServer(("127.0.0.1",8899),Mysrerver)#实例化客户端
server.serve_forever()#让客户端运行起来