class InSig:
    def __init__(self, x, y, name, attitude):
        """
        初始化一个对象的位置、名称和态度。

        参数:
        x (int): 对象在x轴上的位置。
        y (int): 对象在y轴上的位置。
        name (str): 对象的名称。
        attitude (str): 对象的态度，可能是友好、敌对等。

        返回:
        无返回值。该方法用于初始化对象的属性。
        """
        self.x = x
        self.y = y
        self.name = name
        self.attitude = attitude
    def __str__(self):
        """
        重写__str__方法，返回INSIG对象的字符串表示。
    
        该方法包括对象的名称(self.name)、x坐标(self.x)、y坐标(self.y)和态度(self.attitude)。
        这种表示方式便于调试和日志记录，提供了一种一致且易于理解的对象信息展示方式。

        返回:
        str: 包含对象名称、x坐标、y坐标和态度的字符串。
        """
        return f"<INSIG: name: {self.name}, x: {self.x}, y: {self.y}, attitude: {self.attitude}>"
