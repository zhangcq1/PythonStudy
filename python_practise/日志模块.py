import logging
import traceback#导入获取错误信息模块

loger=logging.basicConfig(filename='log.txt',
                           format='%(asctime)s - %(name)s) - %(levelname)s - %(module)s: %(message)s',
                           #format各参数以此为:时间-用户名-类型(debug,info等)-具体py文件-文本信息
                           datefmt='%Y-%m-%d %H:%M:%S',
                           level=10)
logging.debug('测试')#level>10才会执行,写入类型为DEBUG的一条日志,主要是测试相关
logging.info('配置')#level>20执行,写入类型为DEBUG的一条日志,主要是配置相关
logging.warning('警告')#level>30,写入类型为WARNING 的一条日志,主要是警告相关
logging.error('错误')#level>40,写入类型为DEBUG的一条日志,主要是错误相关
logging.critical('严重错误')#level>50,写入类型为CRITICAL 的一条日志,主要是非常严重的错误相关
try:
    a=b
except Exception as ele:
    #traceback.format_exc(), 获取当前错误的堆栈信息
    logging.error(traceback.format_exc())#写入日志
