#-----------------------------自定义栈--------------------------------
class Stack(object):
    def __init__(self):#用列表模拟栈
        self.stack = list()
    def is_empty(self):#判断栈是否为空
        return not len(self.stack)
    def push(self,data):#向栈中加入元素
        self.stack.append(data)
    def pop(self):#从栈中取出元素
        if self.is_empty():
            return None
        return self.stack.pop()
    def length(self):#获取栈的长度
        return len(self.stack)
    def top(self):#获取栈的顶部元素
        return self.stack[-1]
    def bottom(self):#获取栈的底部元素
        return self.stack[0]
    def show(self):#获取栈中所有元素
        if self.is_empty():
            return None
        return 'bottom|'+'|'.join([str(x) for x in self.stack])+'|top'
if __name__ == '__main__':

    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack.is_empty())
    print(stack.top())
    print(stack.bottom())
    print(stack.pop())
    print(stack.length())
    print(stack.show())
