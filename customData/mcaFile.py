from re import match

from _testcapi import INT_MAX

import re

from staticFileds import LOGGER, REGION_SAVE_RANGE


class MCAFile:
    name = ""
    x = INT_MAX
    z = INT_MAX
    needSave = False

    def __init__(self, fileName):
        self.name = fileName
        self.parseFileName()
        self.checkNeedSave()


    def parseFileName(self):
        """
        根据文静名处理
        :return:
        """
        pattern = r"^r\.(\-?\d+)\.(\-?\d+)\.mca"
        matchName = re.match(pattern, self.name)
        if matchName:
            LOGGER.info(f"匹配到mca文件, x: {matchName.groups()[0]}, z: {matchName.groups()[1]}")
            self.x = int(matchName.groups()[0])
            self.z = int(matchName.groups()[1])

    def checkNeedSave(self):
        saveRange = REGION_SAVE_RANGE
        if (saveRange[0] <= self.x <= saveRange[-1]) and (saveRange[0] <= self.z <= saveRange[-1]):
            self.needSave = True