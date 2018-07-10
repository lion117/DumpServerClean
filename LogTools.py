# -*- coding: utf-8 -*-

import sys, os, time
import logging


# create g_logger
logger_name = "logtool"
g_logger = logging.getLogger(logger_name)
g_logger.setLevel(logging.DEBUG)
# create file handler
log_path = "pyInfo.log"
fh = logging.FileHandler(log_path)
fh.setLevel(logging.WARN)
# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)
# add handler and formatter to g_logger
fh.setFormatter(formatter)
ConsoleHanle = logging.StreamHandler()
g_logger.addHandler(ConsoleHanle)
g_logger.addHandler(fh)

class MainRun():
    @staticmethod
    def runLog():
        # print log info
        g_logger.debug('debug message')
        g_logger.info('info message')
        g_logger.warn('warn message')
        g_logger.error('error message')
        g_logger.critical('critical message')


if __name__ == "__main__":
    # print(os.getcwd())
    MainRun.runLog()