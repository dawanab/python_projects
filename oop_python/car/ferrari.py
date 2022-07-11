from car import Car

class Ferrari(Car):
    def __init__(self, __cylinders, __name):
        super().__init__(__cylinders, __name)
    
    def start_engine(self):
        return "Ferrari -> start_engine()"

    def accelerate(self):
        return "Ferrari -> accelerate()"

    def brake(self):
        return "Ferrari -> brake()"

ferrari = Ferrari(4, "Roma")
print(ferrari.start_engine())
print(ferrari.accelerate())
print(ferrari.brake())  
print(f"Cylinder = {ferrari.get_cylinder()}")
print(f"Name = {ferrari.get_name()}")
print(f"Engine = {ferrari.is_engine()}")
