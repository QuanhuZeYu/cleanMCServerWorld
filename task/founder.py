import os
from typing import List

import staticFileds
from customData.mcaFile import MCAFile
from staticFileds import LOGGER


def findAllDIMFolders(worldPath):
    """
    找到所有需要处理的DIM文件夹
    :param worldPath:
    :return: 绝对路径列表
    """
    prefixes = staticFileds.FOLDER_PREFIX
    findTarget: List[str] = []
    mainRegion = os.path.join(worldPath)
    if(os.path.exists(mainRegion)):
        findTarget.append(mainRegion)
    else:
        LOGGER.warning(f"未找到主世界Region: {mainRegion}")
    try:
        dirs = os.listdir(worldPath)
    except Exception as e:
        LOGGER.warning(f"遍历文件夹时失败: {e}")
        quit()
    for fDir in dirs:
        for prefix in prefixes:
            if fDir.startswith(prefix):
                fDir = os.path.join(worldPath, fDir)
                LOGGER.info(f"找到目标文件夹: {fDir}")
                findTarget.append(fDir)
    return findTarget

def findMCAFiles(dimFolder):
    """
    找到该DIM文件夹下的所有mca文件
    :param dimFolder:
    :return:mcaFiles 绝对路径列表
    """
    # 先前往region文件夹
    regionFolder = os.path.join(dimFolder, "region")
    # 遍历文件
    mcaFiles = []
    try:
        files = os.listdir(regionFolder)
    except Exception as e:
        str = f"在{dimFolder}中未找到region文件夹"
        raise str
    for file in files:
        if file.endswith(".mca"):
            mcaFiles.append(os.path.join(regionFolder, file))
    LOGGER.info(f"在{os.path.basename(dimFolder)}中找到{len(mcaFiles)}个mca文件")
    return mcaFiles



if __name__ == '__main__':
    targets = findAllDIMFolders(
        r"D:\Docker\MC\Server\GT_New_Horizons_2.7.0-beta-2--2024-11-1之后记得删除\World")
    mcaFiles = findMCAFiles(targets[0])