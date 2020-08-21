import logging
import traceback#导入获取错误信息模块

def SetLogger(logger_name,file_name):
    #定义一个函数给,传入日志对象名字和存放日志的文件名  
    file_handler=logging.FileHandler(file_name,'a',encoding='utf-8')
    #创建存放日志的文件
    file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s) - %(levelname)s - %(module)s: %(message)s'))
    #设置日志写入的格式
    logger_name=logging.Logger(logger_name,level=logging.ERROR)
    logger_name.addHandler(file_handler)
    return logger_name#返回日志管理对象

logger1=SetLogger('logger1','log1.txt')#拿到名为logger1的日志管理对象
logger2=SetLogger('logger2','log2.txt')#拿到名为logger2的日志管理对象
try:
    a=b
except Exception as ele:
    #traceback.format_exc(), 获取当前错误的堆栈信息
    logger1.error(traceback.format_exc())#在对象logger1中写入日志
    logger2.error(traceback.format_exc())#在对象logger2中写入日志
