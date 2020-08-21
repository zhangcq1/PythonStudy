import time

def fun():
    while 1:
        time.sleep(1)
        struct_time=time.localtime()
        ret='\r%s'%time.strftime('%H:%M:%S',struct_time)
        print(ret,end='',flush=True)
def fun_print():
    print(1111)
if __name__ == '__main__':
    fun()
