# -*- coding: utf-8 -*-

import sys, os, time
import datetime
import platform
from  LogTools import g_logger


def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)

def convertDateFormat(tTime):
    tTime = time.localtime(tTime)
    return  datetime.datetime(tTime.tm_year, tTime.tm_mon,tTime.tm_mday,tTime.tm_hour,tTime.tm_min,tTime.tm_sec)


def getFileCreateTime(filePath):
    t = os.path.getctime(filePath)
    return convertDateFormat(t)


'''获取文件的修改时间'''

def getFileModifyTime(filePath):
    t = os.path.getmtime(filePath)
    return convertDateFormat(t)



def getFileOutDays(tFile):
    if os.path.exists(tFile) is False:
        g_logger.error(u"file is not exist: %s"%(tFile))
    lT1 = getFileCreateTime(tFile)
    lT2 = datetime.datetime.now()
    lDays  = (lT2 - lT1).days
    # print(lDays)
    return  lDays


def walkDir(tDir):
    if os.path.exists(tDir) is False:
        g_logger.error(u"dir is not exist: %s" % (tDir))
        return
    lList = []
    for (dirpath, dirnames, filenames) in os.walk(tDir):
        for itorFile in filenames:
            lList.append(itorFile)
    return lList

def getFileShelfLife(tFile):
    if os.path.exists(tFile) is False:
        g_logger.error(u"file is not exist: %s" % (tFile))
        return
    lPcmFilter = u"PCM_"
    lDumpFilter = u"FxPartner_CrashDump_V"
    lHijackFilter = u"Hijacking_"
    lFaceFilter = u"FACE_"
    lLogFilter = u"Log_"
    if tFile.find(lPcmFilter) != -1:
        return 15
    if tFile.find(lDumpFilter) != -1:
        return 60
    if tFile.find(lHijackFilter) != -1:
        return 60
    if tFile.find(lFaceFilter) != -1:
        return 30
    if tFile.find(lLogFilter) != -1:
        return 60
    return 60


def doBussiness():
    sysstr = platform.system()
    if(sysstr =="Windows"):
        lWorkDir = os.getcwd()
    else:
        lWorkDir = u"/var/www/html/fxupload"
    lFileList = walkDir(lWorkDir)
    lIndex = 0
    for itor in lFileList:
        lLifeDays = getFileOutDays(itor)
        lAllowDays = getFileShelfLife(itor)
        if lLifeDays > lAllowDays:
            lIndex +=1
            print(itor)
            #os.remove(itor)
    g_logger.info(u"remove files counts: %d "%(lIndex))

def watchDog():
    lLastDate = datetime.datetime(2018,01,01,0,0,0)
    lSleepTime = 5
    while(True):
        lToday = datetime.datetime.today()
        if (lToday- lLastDate ).seconds > 15:
            lLastDate = lToday
            doBussiness()
            g_logger.info(u"do bussiness")
            time.sleep(lSleepTime)
        else:
            time.sleep(lSleepTime)
            g_logger.info(u"sleep")


class MainRun():
    @staticmethod
    def runGetModifyTime():
        lFile = u"FilesCleaner.py"
        lT = getFileModifyTime(lFile)
        print(lT)


    @staticmethod
    def runGetCreateTime():
        lFile = u"FilesCleaner.py"
        lT = getFileCreateTime(lFile)
        print(lT)


    @staticmethod
    def runComputeTimeDiff():
        lFile = u"FilesCleaner.py"
        lT1 = getFileCreateTime(lFile)
        lT2 = datetime.datetime.now()
        print(lT1)
        print(lT2)
        print((lT2 - lT1).days)


    @staticmethod
    def rungetFileOutDays():
        lFile = u"FilesCleaner.py"
        print(getFileOutDays(lFile))

    @staticmethod
    def runWatchDog():
        watchDog()

if __name__ == "__main__":
    print(os.getcwd())
    # MainRun.runGetModifyTime()
    # MainRun.runGetCreateTime()
    # MainRun.runComputeTimeDiff()
    # MainRun.rungetFileOutDays()
    MainRun.runWatchDog()