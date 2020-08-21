#-----------------------------自定义双向链表--------------------------------
class Item(object):#定义链表的每一个节点
    def __init__(self,data,last=None,next=None,):
        self.data = data #以字典形式,存放数据
        self.last = last#用于指向上一个节点
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
        body = Item(data,last=sign)#用传过来的数据实例化一个节点对象,last指向链表尾部
        sign.next = body #连接到链表尾部

    def move(self,keyword,keyvalue):#根据关键词,删除一个节点
        sign = self.head.next #游标,判断链表走到哪里了
        status = True #状态,判断是否找到了符合要求的的节点
        while True:
            try:
                if keyvalue == sign.data[keyword]:#根据关键词查找是否存在该节点
                    break
            except KeyError as e:#如果关键词有误,抛出异常并返回False
                print('Key1Error:数据中不存在%s' %e )
                return False
            if sign.next == None:#如果走到链表尾部,说明没有找到该节点
                status = False
                break
            sign = sign.next
        if status:#如果删除成功,返回True,不成功返回False
            sign.last.next = sign.next
            if sign.next != None:
                sign.next.last = sign.last
            sign.last = None
            return True
        else:
            return False


    def update(self,data,keyword=None,keyvalue=None):#修改节点数据
        if keyword:#定位节点
            sign = self.head.next
            status = True
            while True:
                try:
                    if keyvalue == sign.data[keyword]:
                        break
                except KeyError as e:  # 如果关键词有误,抛出异常并返回False
                    print('Key1Error:数据中不存在%s' % e)
                    return False
                if sign.next == None:
                    status = False
                    break
                sign = sign.next
            if status:#更新data数据
                sign.data = data
                return True
            else:
                return False

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



linked_list = LinkedList()
linked_list.add({'name':'a','age':11})
linked_list.add({'name':'b','age':2})
linked_list.add({'name':'c','age':31})
print(linked_list.get_all())
# print(linked_list.size())
# print(linked_list.get(1))
# print(linked_list.get_all())
stats = linked_list.move(keyword='age',keyvalue=2)
print(linked_list.get_all())
# stats = linked_list.move(keyword='age',keyvalue=31)
# print(linked_list.get_all())

print(linked_list.update({'name':'ddd','age':100},keyword='age',keyvalue=31))
print(linked_list.get_all())

#-----------------------------自定义单向循环链表--------------------------------
class Item(object):#定义链表的每一个节点
    def __init__(self,data,next=None,):
        self.data = data #编号
        self.next = next #用于指向下一个节点

class CycleLinkedList(object): #实现环形链表的主要结构与各功能
    def __init__(self):
        self.first = Item(None,next=None)#定义链表开始位置,方便遍历
        self.first.next = self.first

    def add(self,N,): #根据N值创建一个节点为N的环形链表
        sign = self.first
        for data in range(1,N+1):
            if sign.data == None:
                sign.data = data
            else:
                while True:
                    if sign.next == self.first:
                        break
                    sign = sign.next
                body = Item(data)
                sign.next = body
                body.next = self.first


    def move(self,K):#根据关键词K,将指针移到编号K位置,并且返回该指针
        sign1 = self.first #定位编号为K的节点
        sign2 = self.first #定位编号为K的节点的上一个节点,方便对链表进行操作
        while True:
            if sign2.next == self.first:
                break
            sign2 = sign2.next
        while K >1:
            sign1 = sign1.next
            sign2 = sign2.next
            K -= 1
        return sign1,sign2

    def pop(self,sign1,sign2,M):#按照当前节点从1开始计数,当计数为M的节点进行删除
        res = [] #收集删除的节点编号
        while sign1 != sign2:
            num = M
            while num > 1:
                sign1 =sign1.next
                sign2 = sign2.next
                num -= 1
            res.append(sign1.data)
            sign2.next = sign1.next
            sign1 = sign1.next
        res.append(sign1.data)
        return res
    def show(self):
        sign = self.first
        res = []
        while True:
            res.append(sign.data)
            if sign.next == self.first:
                break
            sign = sign.next
        return res

def main(N,K,M):
    peoples = CycleLinkedList()
    peoples.add(N)
    sign1,sign2 = peoples.move(K)
    print(peoples.pop(sign1,sign2,M))
if __name__ == '__main__':
    main(8,1,4)
