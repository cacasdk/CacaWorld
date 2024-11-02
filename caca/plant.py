from caca.caca import Caca

class Plant(Caca):
    def __init__(self, x, y, _world, weight):
        """
        初始化植物类实例。

        参数:
        x: 植物的x坐标。
        y: 植物的y坐标。
        _world: 植物所属的世界环境对象。
        weight: 植物的重量。

        返回值:
        无返回值。
        """
        # 调用父类Caca的构造方法，初始化植物实例。
        Caca.__init__(self, x, y, _world, weight, 0)
        # 设置植物的类型为"PLANT"。
        self.CACA_TYPE = "PLANT"
        # 为植物设置形状为圆形。
        self.turtle.shape("circle")
        # 将植物移动到指定的坐标位置。
        self.turtle.goto(self.x, self.y)
        # 将植物的颜色设置为绿色。
        self.turtle.color("green")