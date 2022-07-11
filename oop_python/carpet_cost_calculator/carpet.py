# from floor import *

class Carpet:
    def __init__(self, _cost):
        if _cost < 0:
            self._cost = 0
        else:
            self._cost = _cost
        
    def get_cost(self):
        return self._cost



