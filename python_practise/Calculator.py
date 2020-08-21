import time#获取程序运行时间
start = time.clock()

class Calculator(object):
    '''这是一个四则混合运算计算器 Calculator 2.0'''
    def __init__(self):
        self.name = Calculator
        self.formula=input('Please input formula:')#让用户输入公式
        self.formula_list=[]
        self.formula_list1=[]#定以两个个空列表,用于数据的转换处理



    def main(self):#主函数,主要处理括号运算
        self.formula_list=list(self.formula)#将用户输入的运算式转换成列表,储存在self.formula_list,方便进行处理
        num = 0#用来遍历formula_list
        Sum=''#收集()内容
        while num<len(self.formula_list):
            while '(' in self.formula_list:
                if self.formula_list[num]==')' and self.formula_list[num-1].isdigit():
                    num1=num-1
                    while self.formula_list[num1]!='(':
                        Sum = Sum+self.formula_list[num1]
                        num1=num1-1
                        
                    else:
                        self.formula_list1=self.formula_list
                        self.formula_list=list(Sum[::-1])
                        nums = self.DealOper()
                        self.formula_list1[num1:num+1]=[nums]
                        self.formula_list=self.formula_list1
                        self.formula_list1=[]
                        Sum=''
                        num=0
                else:
                    num=num+1
            else:
                print(self.DealOper())
                break


    def Fun_Mul(self):
    #计算公式中所有乘法运算
        
        if '*' in self.formula_list:
            i=0
            while i<len(self.formula_list):
                if self.formula_list[i] == '*' and (i+2)!=len(self.formula_list):
                    Sum=int(self.formula_list[i-1])*int(self.formula_list[i+1])
                    self.formula_list[(i-1):(i+2)]=[str(Sum)]
                    i=i-2
                elif self.formula_list[i] == '*' and (i+2)==len(self.formula_list):
                    Sum=int(self.formula_list[i-1])*int(self.formula_list[i+1])
                    self.formula_list[(i-1):]=[str(Sum)]    
                    
                else:
                    i=i+1

                
    def Fun_Div(self):
    #计算公式中所有除法运算
        if '/' in self.formula_list:
            i=0
            while i<len(self.formula_list):
                if self.formula_list[i] == '/' and (i+2)!=len(self.formula_list):
                    Sum=int(self.formula_list[i-1])//int(self.formula_list[i+1])
                    self.formula_list[(i-1):(i+2)]=[str(Sum)]
                    i=i-2
                elif self.formula_list[i] == '/' and (i+2)==len(self.formula_list):
                    Sum=int(self.formula_list[i-1])//int(self.formula_list[i+1])
                    self.formula_list[(i-1):]=[str(Sum)]    
                    
                else:
                    i=i+1


                
    def Fun_Sub(self):
    #计算公式中所有减法法运算
        if '-' in self.formula_list:
            i=0
            while i<len(self.formula_list):
                if self.formula_list[i] == '-' and (i+2)!=len(self.formula_list):
                    Sum=int(self.formula_list[i-1])-int(self.formula_list[i+1])
                    self.formula_list[(i-1):(i+2)]=[str(Sum)]
                    i=i-2
                elif self.formula_list[i] == '-' and (i+2)==len(self.formula_list):
                    Sum=int(self.formula_list[i-1])-int(self.formula_list[i+1])
                    self.formula_list[(i-1):]=[str(Sum)]    
                    
                else:
                    i=i+1
        
                

        
    def DealFormula(self):
        #将计算式由字符串转成列表,并对其包含的多位数进行处理
        #self.formula_list=list(self.formula)
        sud=['+','-','*','/',]
        num = 0
        Sum=''
        while num<len(self.formula_list):
            if self.formula_list[num].isdigit():
                Sum=Sum+self.formula_list[num]
                num=num+1
                if num==len(self.formula_list) and self.formula_list[num-2].isdigit():
                    buc=len(Sum)
                    self.formula_list[(num-buc):num]=[Sum]
                continue
            elif self.formula_list[num] in sud:
                buc=len(Sum)
                self.formula_list[(num-buc):num]=[Sum]
                Sum=''
                num=num+1-(buc-1)
                continue
            else:
                break


    def DealOper(self):
        
        #主函数,经过乘,除,减法运算后,计算式中只剩加法运算,对其进行累加
        self.DealFormula()
        self.Fun_Mul()
        self.Fun_Div()
        self.Fun_Sub()
        if '+' in self.formula_list:
            result = 0
            for number in self.formula_list:
                
                if number =='+':
                    continue    
                else:
                    result=result+int(number)
            return str(result)
        
        elif len(self.formula_list)==1:
            return str(self.formula_list[0])
            



        

calculator=Calculator()
calculator.main()


END=input('Enter any key to return')#防止程序闪退
end = time.clock()
print('Running time:' ,(end-start))
