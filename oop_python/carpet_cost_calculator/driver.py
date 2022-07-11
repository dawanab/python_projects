
from calculator import Calculator
from carpet import Carpet
from floor import *


carpet = Carpet(12.06)
floor = Floor(2.12, 5.06)
calculator = Calculator(floor, carpet)
print(f"Total = ${calculator.get_total_cost()}")


