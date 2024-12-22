import math

from brain_sig import *


class World:
    """
    表示一个包含多个小动物的世界。
    """

    def __init__(self):
        self.cacas = []

    def add_caca(self, caca):
        """
        向世界中添加一个小动物。

        参数:
        Cacas (Caca): 要添加的小动物对象。

        返回:
        无返回值。
        """
        self.cacas.append(caca)

    def remove_caca(self, caca_name):
        """
        从世界中移除一个小动物。

        参数:
        caca_name (str): 要移除的小动物的名字。

        返回:
        bool: 如果成功移除返回True，否则返回False。
        """
        for caca in self.cacas:
            if caca.name == caca_name:
                self.cacas.remove(caca)
                return True
        return False

    def list_cacas(self):
        """
        列出世界中的所有小动物。

        返回:
        list: 包含所有小动物的列表。
        """
        return self.cacas

    def find_nearest_caca(self, target_caca):
        """
        寻找与目标小动物最接近的小动物。

        如果没有小动物或只有一个小动物，则无法进行比较，将返回None或抛出异常。

        参数:
        target_caca: 需要比较的小动物对象。

        返回:
        返回最接近目标小动物的小动物对象，如果没有找到或无法进行比较，则返回None。
        """
        # 检查是否有小动物存在
        if not self.cacas:
            raise ValueError("没有小动物")

        # 如果只有一个小动物，无法进行比较，根据需求选择返回None或抛出异常
        if len(self.cacas) == 1:
            return None  # 或者根据需求选择抛出异常

        # 初始化最近的小动物和最小的距离平方
        nearest_caca = None
        min_distance_squared = float('inf')

        # 遍历所有小动物，寻找最近的小动物
        for other_caca in self.cacas:
            # 如果是目标小动物，跳过，避免自己与自己比较
            if target_caca == other_caca:
                continue

            # 计算当前小动物与目标小动物的距离平方
            distance_squared = (target_caca.x - other_caca.x) ** 2 + (target_caca.y - other_caca.y) ** 2
            # 如果当前距离平方小于已知的最小距离平方，更新最小距离平方和最近的小动物
            if distance_squared < min_distance_squared:
                min_distance_squared = distance_squared
                nearest_caca = other_caca

        # 返回最近的小动物
        return nearest_caca

    def __str__(self):
        """
        返回世界的字符串表示。

        返回:
        str: 包含世界中所有小动物的字符串。
        """
        return "World with cacas:\n" + "\n".join(str(caca) for caca in self.cacas)

    def generate(self):
        for caca in self.cacas:
            # 找到距离caca几何距离最近的另一caca
            nearest_caca = self.find_nearest_caca(caca)

            caca.brain(InSig(nearest_caca.x, nearest_caca.y, nearest_caca.name, ))