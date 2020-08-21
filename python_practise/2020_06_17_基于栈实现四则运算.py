#-----------------------------基于栈实现四则运算--------------------------------
class Stack(object):
    def __init__(self):  # 用列表模拟栈
        self.stack = list()
    def is_empty(self):  # 判断栈是否为空
        return not len(self.stack)
    def push(self, data):  # 向栈中加入元素
        self.stack.append(data)
    def pop(self):  # 从栈中取出元素
        if self.is_empty():
            return None
        return self.stack.pop()
    def length(self):  # 获取栈的长度
        return len(self.stack)
    def top(self):  # 获取栈的顶部元素
        return self.stack[-1]
    def bottom(self):  # 获取栈的底部元素
        return self.stack[0]
    def show(self):  # 获取栈中所有元素
        if self.is_empty():
            return None
        return 'bottom|' + '|'.join([str(x) for x in self.stack]) + '|top'



class Calcullator(object):
    def __init__(self):
        pass

    def main(self, formula):
        numbers = Stack()
        signs = Stack()
        length = len(formula) - 1
        sign = 0
        while sign <= length:
            ele = formula[sign]
            num = ''
            while ele.isdigit():
                num += ele
                sign += 1
                if sign > length:
                    break
                ele = formula[sign]

            if sign > length:
                numbers.push(num)
                break
            numbers.push(num)

            if signs.is_empty():
                signs.push(ele)
                sign += 1

            elif self.rule(ele) <= self.rule(signs.top()):
                numbers.push(self.operation(signs.pop(), int(numbers.pop()), int(numbers.pop())))
                signs.push(ele)
                sign += 1

            else:
                signs.push(ele)
                sign += 1
        print(numbers.show(),signs.show())
        while not signs.is_empty():
            numbers.push(self.operation(signs.pop(), int(numbers.pop()), int(numbers.pop())))
        print(numbers.top())

    def operation(self,symbol,num2,num1):
        if symbol =='+':
            return num1+num2
        if symbol =='-':
            return num1-num2
        if symbol =='*':
            return num1*num2
        if symbol =='/':
            return num1//num2
    def rule(self,symbol):
        if symbol == '*' or symbol =='/':
            return 2
        if symbol == '+' or symbol =='-':
            return 1



formula = '100+100*2/2*2+20*30+400*3'
cal = Calcullator()
cal.main(formula)
