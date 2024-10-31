import time
from world import World
class Animal:
    def __init__(self,name:str='CACA_{0}'.format(str(time.time())),world:World)->None:

        self.name=name
        self.world=world
    def