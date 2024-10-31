class InSig:
    def __init__(self, x, y, name, attitude):
        self.x = x
        self.y = y
        self.name = name
        self.attitude = attitude
    def __str__(self):
        return f"<name: {self.name}, x: {self.x}, y: {self.y}, attitude: {self.attitude}>"
