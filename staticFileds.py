import os

from logger.logger import createLogger

# 当前目录绝对路径
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# 一些常量值
CHUNK_LENGTH = 16
REGION_LENGTH = 512

# 需要的范围为 -5~+5
REGION_SAVE_RANGE = range(-5, 6) # 为什么是6？ 因为range(5)是[0,1,2,3,4]

# 遍历时需要带有的前缀
FOLDER_PREFIX = ["DIM"]

# 日志
LOG_DIR = os.path.join(ROOT_DIR, "log")
LOG_FILE = os.path.join(LOG_DIR, "latest.log")
LOGGER = createLogger()