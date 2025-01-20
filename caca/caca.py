class Caca:
    """
    Caca类代表一个在特定世界中的小动物，具有位置、体力值和视力等属性。
    该类使用turtle图形库来在图形界面上表示小动物的位置和状态。
    """
    def __init__(self, x:float, y:float, weight:float, visible:float):
        """
        初始化Caca小动物的属性。

        :param x: 小动物的初始x坐标。
        :param y: 小动物的初始y坐标。
        :param weight: 小动物的初始体力值，表示小动物的体力状况。
        :param visible: 小动物的视力状态，表示小动物的可见范围。
        """
        self.visible = visible  # 设置实体的视力状态
        self.x = x  # 设置实体的x坐标
        self.y = y  # 设置实体的y坐标
        self.weight = weight  # 设置实体的体力值
    def __str__(self):
        return f"Caca({self.x}, {self.y}, {self.weight}, {self.visible})"
