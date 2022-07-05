class Car:
    __engine = True
    __wheels = 4

    def __init__(self, __cylinders, __name):
        self.__cylinders = __cylinders
        self.__name = __name

    def start_engine(self):
        return "The car's engine is running..."

    def accelerate(self):
        return "The car is accelerating."

    def brake(self):
        return "The car is breaking."

    def get_name(self):
        return self.__name

    def get_cylinder(self):
        return self.__cylinders
    
    def get_wheels(self):
        return self.__wheels
    
    def is_engine(self):
        return self.__engine


        