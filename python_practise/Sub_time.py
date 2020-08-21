import time
def Sub_time(Time):
    time1=time.time()
    S_Time=time.strptime(Time,'%Y-%m-%d %H:%M:%S')
    time2=time.mktime(S_Time)     
    res=abs(time1-time2)
    r_time=time.gmtime(res)
    ret=(r_time.tm_year-1970,r_time.tm_mon-1,r_time.tm_mday-1,\
         r_time.tm_hour,r_time.tm_min,r_time.tm_sec)
    if time1>time2:
        print('你输入的时间已经过去了:%s年%s月%s日 %s时:%s分:%s秒'%ret)
    if time1<time2:
        print('距你输入的时间还有:%s年%s月%s日 %s时:%s分:%s秒'%ret)
Time='2018-4-26 0:0:0'
Sub_time(Time)
Time='2020-3-17 0:0:0'
Sub_time(Time)
