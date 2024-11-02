from world import World
from turtle import Turtle

class Caca:
    def __init__(self, x:int, y:int, _world:World, weight:int, visible:float)->None:
        self.x = 0
        self.y = 0

        self.weight = 10
        self.turtle = Turtle()
        ...
    def die(self)->None: ...
    def eat(self,food:int): ...


