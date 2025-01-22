from typing import Optional, List
import logging
from pathlib import Path

# 假设 caca 是一个已定义的模块
import caca.caca as caca

# 配置日志
logger = logging.getLogger('WorldLogger')
logger.setLevel(logging.INFO)

# 确保日志目录存在
log_dir = Path('logs')
log_dir.mkdir(exist_ok=True)
log_file = log_dir / 'world.caca.log'

# 创建一个文件处理器，将日志写入文件
file_handler = logging.FileHandler(log_file, mode='a')
file_handler.setLevel(logging.INFO)

# 创建一个格式化器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将文件处理器添加到 Logger 对象
logger.addHandler(file_handler)

class World(List[caca.Caca]):
    def __init__(self, height: float, width: float):
        """
        初始化世界对象。

        参数:
        - height (float): 世界的高度。
        - width (float): 世界的宽度。
        """
        super().__init__()
        self.height: float = height
        self.width: float = width

        logger.info(f"World initialized with height={height} and width={width}")

    def append(self, new_caca: caca.Caca):
        """
        向世界中添加一个新的caca对象。

        参数:
        - new_caca (Caca): 要添加到世界的新的caca对象。
        """
        super().append(new_caca)
        logger.info(f"Added new caca object to the world. Total cacas: {len(self)}")

    def pop(self, index: int | None = -1) -> caca.Caca:
        """
        从世界中移除一个caca对象。

        参数:
        - index (int | None): 要移除的caca对象在列表中的索引，默认为-1（最后一个元素）。
        """
        try:
            removed_caca = super().pop(index if index is not None else -1)
            logger.info(f"Removed caca object with id {index}. Total cacas: {len(self)}")
            return removed_caca
        except IndexError:
            logger.error(f"Failed to remove caca object at index {index}: Index out of range")
            raise IndexError("Index out of range")
