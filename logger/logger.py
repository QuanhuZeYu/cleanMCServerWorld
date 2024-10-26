import loguru
import os

import staticFileds


def checkLogDir():
    rootDir = staticFileds.ROOT_DIR
    # 检查目录下是否有log文件夹
    logDir = os.path.join(rootDir, "log")
    if not os.path.exists(logDir):
        os.mkdir(logDir)

def checkLogFile():
    # 检查latest.log文件是否存在, 存在则删除它
    rootDir = staticFileds.ROOT_DIR
    logDir = os.path.join(rootDir, staticFileds.ROOT_DIR)
    latestLog = os.path.join(logDir, staticFileds.LOG_FILE)
    if os.path.exists(latestLog):
        os.remove(latestLog)

def createLogger():
    checkLogDir()
    checkLogFile()
    logger = loguru.logger
    logger.add(staticFileds.LOG_FILE, rotation="500 MB", encoding="utf-8")
    return logger
