from floor import *
from carpet import Carpet 

class Calculator:
    def __init__(self, _floor, _carpet):
        self.floor = _floor
        self.carpet = _carpet

    def get_total_cost(self):
        return str(round(self.floor.get_area() * self.carpet.get_cost(), 2))