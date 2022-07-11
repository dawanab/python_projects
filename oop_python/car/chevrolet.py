from car import Car

class Chevrolet(Car):
    def __init__(self, __cylinders, __name):
        super().__init__(__cylinders, __name)
    
    def start_engine(self):
        return "Chevrolet -> start_engine()"

    def accelerate(self):
        return "Chevrolet -> accelerate"
    
    def brake(self):
        return "Chevrolet -> brake()"  

chevrolet = Chevrolet(4, "Tahoe")
print(chevrolet.start_engine())
print(chevrolet.accelerate())
print(chevrolet.brake())  
print(f"Cylinder = {chevrolet.get_cylinder()}")
print(f"Name = {chevrolet.get_name()}")
print(f"Engine = {chevrolet.is_engine()}")