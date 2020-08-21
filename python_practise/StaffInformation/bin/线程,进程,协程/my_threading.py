from concurrent.futures import ThreadPoolExecutor
import threading

import time
pool = ThreadPoolExecutor(2)#创建线程池,设置可用的线程个数
def one(arg):
    ret = threading.current_thread()
    print('one %s : %s' % (arg, ret)) #输出当前线程
    v=[]
    v[1] #制造错误
def two(arg):
    time.sleep(2)
    ret = threading.current_thread() #输出当前线程
    print('two %s : %s' % (arg, ret))

for i in range(1,11):
    pool.submit(one,i) #从线程池中申请一个线程执行函数one,
    #如果线程池中有空闲的线程,则申请成功,如果没有,就等待线程完成任务后申请执行

for i in range(1,11):
    pool.submit(two,i,)#pool.submit(函数,参数),源码:def submit(self, fn, *args, **kwargs):
