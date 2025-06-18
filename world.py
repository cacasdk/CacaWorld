import cacas.caca as caca

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
