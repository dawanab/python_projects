from hamburger import Hamburger

class HealthyBurger(Hamburger):
    def __init__(self, __meat, __price):
        super().__init__("Healthy",__meat, __price, "White")

    def add_healthy_addition_1(self, name, price):
        self.__healthy_extra_1_name = name
        self.__healthy_extra_1_price = price
    
    def add_healthy_addition_2(self, name, price):
        self.__healthy_extra_2_name = name
        self.healthy_extra_2_price = price 
    
    def itemize_hamburger(self):
        hamburger_price = super().itemize_hamburger()
        if self.__healthy_extra_1_name is not None:
            hamburger_price += self.__healthy_extra_1_price
            print(f"Added {self.__healthy_extra_1_name} = {self.__healthy_extra_1_price}")
        
        if self.__healthy_extra_2_name is not None:
            hamburger_price += self.healthy_extra_2_price
            print(f"Added {self.__healthy_extra_2_name} = {self.healthy_extra_2_price}")
        
        return hamburger_price
            

healthy_burger = HealthyBurger("Beef", 19.99)
healthy_burger.itemize_hamburger()
