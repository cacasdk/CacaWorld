import turtle
import math


class Caca:
    """
    Caca类代表一个在特定世界中的小动物，具有位置、体力值和视力等属性。
    该类使用turtle图形库来在图形界面上表示小动物的位置和状态。
    """
    def __init__(self, x, y, _world, weight, visible):
        """
        初始化Caca小动物的属性。

        :param x: 小动物的初始x坐标。
        :param y: 小动物的初始y坐标。
        :param _world: 小动物所属的世界实例，用于小动物与世界之间的交互。
        :param weight: 小动物的初始体力值，表示小动物的体力状况。
        :param visible: 小动物的视力状态，表示小动物的可见范围。
        """
        self.CACA_TYPE = "CACA" # 定义一个常量CACA_TYPE，用于标识或配置特定的类型或行为
        self.turtle = turtle.Turtle()  # 创建turtle图形对象
        self.visible = visible  # 设置实体的视力状态
        self.x = x  # 设置实体的x坐标
        self.y = y  # 设置实体的y坐标
        self.world = _world  # 设置实体所属的世界
        self.weight = weight  # 设置实体的体力值
        self.turtle.speed(0)  # 设置turtle移动速度为最快
        self.turtle.penup()  # 抬起笔，避免绘制轨迹
        self.turtle.goto(x, y)  # 将turtle移动到实体的初始位置
        self.turtle.shape("turtle")  # 设置turtle的形状为龟形
        self.turtle.turtlesize(0.3, 0.3)  # 设置turtle的大小

    def die(self):
        """死亡函数

        该函数用于在对象"死亡"时调用，以隐藏海龟图形并更新其坐标为无穷远
        """
        # 隐藏海龟图形，使其在屏幕上消失
        self.turtle.hideturtle()
        # 将对象的坐标更新为无穷远，象征其已经离开游戏区域
        self.x = math.inf
        self.y = math.inf
    def eat(self, food):
        self.weight += food