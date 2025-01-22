import logging
from pathlib import Path

# 假设 caca 是一个已定义的模块
import caca.caca as caca

# 单例模式确保日志配置只执行一次
def configure_logger():
    if not hasattr(configure_logger, "configured"):
        _logger = logging.getLogger('WorldLogger')
        _logger.setLevel(logging.INFO)

        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        log_file = log_dir / 'world.caca.log'

        file_handler = logging.FileHandler(log_file, mode='a')
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        _logger.addHandler(file_handler)
        configure_logger.configured = True

configure_logger()
logger = logging.getLogger('WorldLogger')

class World:
    def __init__(self, height: float, width: float):
        """
        初始化世界对象。

        参数:
        - height (float): 世界的高度。
        - width (float): 世界的宽度。
        """
        self.height = height
        self.width = width
        self.cacas = []
        logger.info(f"World initialized with height={height} and width={width}")

    def append(self, new_caca: caca.Caca):
        """
        向世界中添加一个新的caca对象。

        参数:
        - new_caca (Caca): 要添加到世界的新的caca对象。
        """
        if not isinstance(new_caca, caca.Caca):
            raise TypeError("new_caca must be an instance of caca.Caca")
        self.cacas.append(new_caca)
        logger.info(f"Added new caca object to the world. Total cacas: {len(self.cacas)}")

    def pop(self, index: int | None = -1) -> caca.Caca:
        """
        从世界中移除一个caca对象。

        参数:
        - index (int | None): 要移除的caca对象在列表中的索引，默认为-1（最后一个元素）。
        """
        try:
            if index is None:
                index = -1
            removed_caca = self.cacas.pop(index)
            logger.info(f"Removed caca object at index {index}. Total cacas: {len(self.cacas)}")
            return removed_caca
        except IndexError:
            logger.error(f"Failed to remove caca object at index {index}: Index out of range")
            raise IndexError("Index out of range")
        except Exception as e:
            logger.error(f"Failed to remove caca object at index {index}: {str(e)}")
            raise

    def __str__(self):
        return f"World(height={self.height}, width={self.width}, size={len(self.cacas)}, cacas={self.cacas})"

    def __repr__(self):
        return f"World(height={self.height}, width={self.width}, cacas={self.cacas})"

    def __getitem__(self, index):
        return self.cacas[index]
