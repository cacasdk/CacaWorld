from Caca import Caca

class Plant(Caca):
    def __init__(self, name, weight, age, x=0, y=0):
        """
        初始化一个特定对象的实例。

        该构造函数不仅接受名称、重量、年龄作为必需参数，还接受x和y坐标作为可选参数，默认于原点(0,0)。

        参数:
        - name: 名称
        - weight: 重量
        - age: 年龄
        - x: X坐标，默认值为0
        - y: Y坐标，默认值为0

        返回值:
        无返回值。
        """
        super().__init__(name, weight, age, x, y)  # 调用父类Movable的构造方法进行初始化
        self.CACA_TYPE = "PLANT"  # 设置当前对象的类型为"PLANT"
    def __str__(self):
        return super().__str__()
    def brain(self, in_sig):
        super().eat(1)
