import caca.caca
from caca import *
import logging


class World(list):
    def __init__(self, height: float, width: float):
        """
        初始化世界对象。

        参数:
        - height (float): 世界的高度。
        - width (float): 世界的宽度。
        """
        self.height: float = height
        self.width: float = width
        self.cacas = []

        # 创建一个 Logger 对象
        self.logger = logging.getLogger('WorldLogger')
        self.logger.setLevel(logging.INFO)

        # 创建一个文件处理器，将日志写入文件
        file_handler = logging.FileHandler('world.caca.log', mode='a')
        file_handler.setLevel(logging.INFO)

        # 创建一个格式化器
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # 将文件处理器添加到 Logger 对象
        self.logger.addHandler(file_handler)

        self.logger.info(f"World initialized with height={height} and width={width}")

    def add(self, new_caca: caca.caca.Caca):
        """
        向世界中添加一个新的caca对象。

        参数:
        - new_caca (Caca): 要添加到世界的新的caca对象。
        """
        self.cacas.append(new_caca)
        self.logger.info(f"Added new caca object to the world. Total cacas: {len(self.cacas)}")

    def remove(self, caca_id: int):
        """
        从世界中移除一个caca对象。

        参数:
        - caca_id (int): 要移除的caca对象在cacas列表中的索引。
        """
        self.cacas.remove(caca_id)
        self.logger.info(f"Removed caca object with id {caca_id}. Total cacas: {len(self.cacas)}")
