from customData.mcaFile import MCAFile
from staticFileds import LOGGER
from task.founder import findAllDIMFolders, findMCAFiles
import os


def runCleaner():
    """
    交互式输入目标world路径
    先寻找所有的region存在文件夹
    再遍历每个region
    寻找不需要保存的进行删除
    :return:
    """
    LOGGER.info("本脚本用于清理world文件夹DIM开头文件中region和主世界region")
    LOGGER.info("在根目录中的staticFiled.py中设置需要保存的range范围, 也就是保存世界中心")
    LOGGER.info("清理之前尽量做好备份, 例如需要清理的world备份先存放几天, 过一段时间确实不需要再彻底删除")
    LOGGER.info("清理请输入world绝对路径!")
    inputPath = input("需要清理的world绝对路径:")
    targetList = findAllDIMFolders(inputPath)
    for target in targetList:
        LOGGER.info(f"开始清理{target}")
        try:
            mcaFiles = findMCAFiles(target)
        except Exception as e:
            LOGGER.warning(f"{target}中可能不存在region")
            continue
        for mcaFile in mcaFiles:
            mca = MCAFile(mcaFile)
            if not mca.needSave:
                LOGGER.info(f"{target}/{mca.name} 不需要保存, 删除中...")
                os.remove(mcaFile)
    LOGGER.info("清理完毕!")