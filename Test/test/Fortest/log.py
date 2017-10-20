#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logging.config

'''
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='/AutoTest/Test/Log/Fortest.log',
                    filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
'''
'''

#1.创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger1 = logging.getLogger()

#2.创建一个handler，用于写入日志文件/输出到控制台
#向控制台中输出日志
ch = logging.StreamHandler()
# 向一个文件输出日志
fh = logging.FileHandler('/AutoTest/Test/Log/test1.log')

#logging.handlers.RotatingFileHandler向文件中输出日志，当文件达到一定大小后，自动 更改当前日志文件，创建一个新的同名日志文件继续输出
#logging.handlers.TimedRotatingFileHandler向文件中输出日志，间隔一定时间就自动创建新的日志文件

3.定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

4.logger添加到handler里面
#logger.addHandler(fh)
logger.addHandler(ch)
#logger1.addHandler(fh)
#logger1.addHandler(ch)

logger.debug('logger debug message')
logger.info('logger info message')
logger.warning('logger warning message')
logger.critical('logger critical message')

logger1.debug('logger1 debug message')
logger1.info('logger1 info message')
logger1.warning('logger1 warning message')
logger1.critical('logger1 critical message')
'''
import os
#获取当前文件所在的文件夹的上级文件夹目录
formdir = os.path.dirname(os.getcwd())

class MyLog:

    def __init__(self):
        logging.config.fileConfig(formdir + "\Fortest\logging.conf")
        self.logger = logging.getLogger("Example")

    def debug(self,msg):
        self.logger.debug(msg)


if __name__=="__main__":
    log = MyLog()
    log.debug("测试输出日志")


'''
logging.config.fileConfig("logging.conf")

logger2 = logging.getLogger("Example")

logger2.debug('logger2 debug message')
logger2.info('logger2 info message')
logger2.warning('logger2 warning message')
logger2.critical('logger2 critical message')

'''