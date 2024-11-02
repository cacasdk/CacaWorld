class World:
    def __init__(self, width, height):
        self.x = width
        self.y = height
        self.world = []

    def add(self, caca):
        self.world.append(caca)
        self.world.sort()

    def generate(self):
        for caca in self.world:
            if caca.CACA_TYPE == "CACA":
                pass
            elif caca.CACA_TYPE == "PLANT":
                caca.eat(1)  # 晒太阳，长高高~
