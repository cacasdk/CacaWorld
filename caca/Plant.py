import math
from Caca import Caca

class Plant(Caca):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)
        self.max_age = math.inf
        self.max_weight = 100
        self.blossom_time = 30
