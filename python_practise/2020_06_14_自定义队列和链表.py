#-----------------------------自定义队列--------------------------------
class Queue(object):
    def __init__(self,size):
        self.size = size#数组的容量,超过后无法保存
        self.queue = []#利用列表实现队列
    def put(self,ele):#put方法,实现向队列中加元素
        if len(self.queue) < self.size:
            self.queue.append(ele)
        else:
            pass
    def get(self):#get方法,实现从队列中取出元素
        try:
            return self.queue.pop(0)
        except:
            return None
    def get_size(self):#get_size获取当前队列长度
        return len(self.queue)
    def get_queue(self):#get_queue获取当前队列所有元素,返回迭代器
        return self.queue_item()
    def queue_item(self):#将当前队列转换成迭代器
        for ele in self.queue:
            yield ele
#-----------------------------自定义链表--------------------------------
class Item(object):#定义链表的每一个节点
    def __init__(self,data,next=None,):
        self.data = data #以字典形式,存放数据
        self.next = next #用于指向下一个节点

class LinkedList(object): #实现链表的主要结构与各功能
    def __init__(self):
        self.head = Item({},)#定义头节点,不存放数据

    def add(self,data): #增加一个节点
        sign = self.head
        while True: #找到sign.next == None,即链表尾部
            if sign.next == None:
                break
            sign = sign.next
        body = Item(data)#用传过来的数据实例化一个节点对象
        sign.next = body #连接到链表尾部

    def move(self,keyword,keyvalue):#根据关键词,删除一个节点
        sign = self.head #游标,判断链表走到哪里了
        status = True #状态,判断是否找到了符合要求的的节点
        while True:
            if sign.next == None:#如果走到链表尾部,说明没有找到该节点
                status = False
                break
            try:
                if keyvalue == sign.next.data[keyword]:#根据关键词查找是否存在该节点
                    break
            except KeyError as e:#如果关键词有误,抛出异常并返回False
                print('Key1Error:数据中不存在%s' %e )
                return False
            sign = sign.next
        if status:#如果删除成功,返回True,不成功返回False
            sign1 = sign.next.next
            sign.next.next=None
            sign.next = sign1
            return True
        else:
            return False


    def update(self,data,keyword=None,keyvalue=None):#修改节点数据
        if keyword:#和删除一样定位节点
            sign = self.head
            status = True
            while True:
                if sign.next == None:
                    status = False
                try:
                    if keyvalue == sign.next.data[keyword]:
                        break
                except KeyError as e:  # 如果关键词有误,抛出异常并返回False
                    print('Key1Error:数据中不存在%s' % e)
                    return False
                sign = sign.next
            if status:#更新data数据
                sign.next.data = data

    def get(self,index):#根据位置查找
        res = self.get_all()#获取到列表形式链表结构
        try:#按照输入的下标查找
            return res[index]
        except:
            return None

    def get_all(self):#查找整个链表数据
        sign = self.head
        res = []
        while True:#遍历整个链表,并转成列表形式
            if sign.next == None:
                if sign.data:
                    res.append(sign.data)
                break
            else:
                if sign.data:
                    res.append(sign.data)
                sign = sign.next
        return res

    def size(self):  #获取链表有效数据个数
        return len(self.get_all())#直接输出列表形式的链表长度即有效数据个数

    def reverse(self):#反转链表
        res = self.reverse_printing()#获取逆序的列表形式链表
        sign1 = self.head#创建游标
        while True:#遍历整个链表,断开各连接,没有指向的数据会被垃圾回收
            if sign1.next == None:
                break
            sign2 = sign1.next
            sign1.next = None
            sign1 = sign2
        sign = self.head
        for ele in res:#根据逆序列表形式链表,重新构建链表
            body = Item(ele)
            sign.next = body
            sign = sign.next
    def sort(self,keyword,):#根据某个数据进行链表排序
        res = self.sort_printing(keyword)#获取排序后列表形式所有数据
        sign1 = self.head

        while True:#同倒序,断开所有连接
            if sign1.next == None:
                break
            sign2 = sign1.next
            sign1.next = None
            sign1 = sign2
        sign = self.head
        for ele in res:#重构列表
            body = Item(ele)
            sign.next = body
            sign = sign.next
    def sort_printing(self,keyword):
        res = self.get_all()#获取列表形式所有数据
        ret = sorted(res, key=lambda x: x[keyword])#利用sorted排序
        return ret
    def reverse_printing(self):
        res = self.get_all()#获取列表形式所有链表数据
        ret =res[::-1]#反转列表
        return ret

linked_list = LinkedList()
linked_list.add({'name':'a','age':11})
linked_list.add({'name':'b','age':2})
linked_list.add({'name':'c','age':31})
print(linked_list.get_all())
# print(linked_list.size())
# print(linked_list.get(1))
# print(linked_list.reverse_printing())
# linked_list.reverse()
# print(linked_list.get_all())
# print(linked_list.sort_printing('age'))
# linked_list.sort('age')
# print(linked_list.get_all())

# linked_list.move(keyword='age',keyvalue=31)
# print(linked_list.get_all())
stats = linked_list.move(keyword='ag',keyvalue=11)
print(stats)
print(linked_list.get_all())
# linked_list.update({'name':'d','age':33},keyword='age',keyvalue=2)
# print(linked_list.get_all())
