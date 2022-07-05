from car import Car

class Jeep(Car):
    def __init__(self, __cylinders, __name):
        super().__init__(__cylinders, __name)

    def start_engine(self):
        return "Jeep -> start_engine()"
    
    def accelerate(self):
        return "Jeep -> accelerate()"
    
    def brake(self):
        return "Jeep -> brake()"

jeep = Jeep(4, "Wrangler")
print(jeep.start_engine())
print(jeep.accelerate())
print(jeep.brake())  
print(f"Cylinder = {jeep.get_cylinder()}")
print(f"Name = {jeep.get_name()}")
print(f"Engine = {jeep.is_engine()}")