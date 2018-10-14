'''
Created on 2018年7月1日

@author: Administrator
'''
import logging      #导入日志模块
import os,time

cur_path = os.path.dirname(os.path.abspath('.'))        #获取当前文件的路径
log_path = os.path.join(cur_path,"logs")        #指定日志存放的目录

class Log():
    def __init__(self):
        #日志文件命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y-%m-%d-%H-%M-%S'))
        self.logger = logging.getLogger()       
        self.logger.setLevel(logging.DEBUG)
        #定义日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d]-fuc:%(funcName)s - %(levelname)s:%(message)s')
    def _console(self,level,message):
        #创建一个FileHandler，用于将日志输出到本地
        fh = logging.FileHandler(self.logname,'a','utf8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个StreamHandler,用于将日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        #判断日志级别
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        #避免日志重复输出的问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self._console('debug',message)
    def info(self,message):
        self._console('info',message)
    def warning(self,message):
        self._console('warning',message)
    def error(self,message):
        self._console('error',message)
if __name__ == '__main__':
    log = Log()
    log.info("--测试开始--")
    log.info('输入密码')
    log.warning('--测试结束--')