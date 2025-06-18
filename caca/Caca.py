import math

class Caca:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age
        self.max_weight = None
        self.max_age = None
        self.blossom_time = math.inf

    def eat(self, food):
        if self.weight + food <= self.max_weight:
            self.weight += food

    def __str__(self):
        return f"{type(self)}(name={self.name}, weight={self.weight}kg, age={self.age} years)"

    class Brain:
        def __init__(self):
            self.importance = None

        def get_signal(self, signal):
            if signal.level > self.importance.level:
                self.importance = signal

        def make_choice(self):
            return None

