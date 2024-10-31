class World:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
        self.world=[]
    def add(self,caca):
        self.world.append(caca)
        self.world.sort()