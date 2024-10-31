import turtle
import math
import caca


class Caca:
    def __init__(self, x, y, _world, weight, visible):
        """
        the init function of the Caca class
        :param x: the x coordinate
        :param y: the y coordinate
        :param _world: the world coordinate
        :param weight: the weight of the caca
        """
        self.visible = visible
        self.x = x
        self.y = y
        self.world = _world
        self.weight = weight
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.shape("turtle")
        self.turtle.turtlesize(0.3, 0.3)

    def die(self):
        """die function of the Caca class"""
        self.turtle.hideturtle()
        self.x = math.inf
        self.y = math.inf
