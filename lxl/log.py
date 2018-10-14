# coding=utf-8
'''
logging模块提供了两种记录日志的方式：
第一种方式是使用logging提供的模块级别的函数
logging.basicConfig(**kwargs)函数用于指定“要记录的日志级别”、“日志格式”、“日志输出位置”、“日志文件的打开模式”等信息
第二种方式是使用Logging日志系统的四大组件
loggers:提供应用程序代码直接使用的接口
handlers:用于将日志记录发送到指定的目的位置
filters:提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）
formatters:用于控制日志信息的最终输出格式
'''
import logging      #导入日志模块
import os
import time,threading

proDir = os.getcwd().split("utils")[0]  
#logs_path = os.path.join(proDir,"logs\\") 
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))       # defined test result file name by localtime
logs_path = proDir + "logs" + os.sep
log_name = logs_path + now + ".log"

class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)     #创建一个logger对象
        self.logger.setLevel(logging.DEBUG)     #define log level
        
        fh = logging.FileHandler(log_name)      #创建一个handle,用于写入日志
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()        #创建一个handler，用于输出到控制台
        ch.setLevel(logging.INFO)
        
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")     #定义handler输出格式
        
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)      #给logger添加handler
        self.logger.addHandler(ch)
    
    def getlog(self):
        return self.logger
'''
创建logger
创建handler
定义formatter
给handler添加formatter
给logger添加handler
logger可以看做是一个记录日志的人，对于记录的每个日志，他需要有一套规则，比如记录的格式（formatter），等级（level）等等，
这个规则就是handler。使用logger.addHandler(handler)添加多个规则，就可以让一个logger记录多个日志
'''      
   
class MyLog:
    log = None
    mutex = threading.Lock()
    
    def __init__(self):
        pass
    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Logger()
            MyLog.mutex.release()  