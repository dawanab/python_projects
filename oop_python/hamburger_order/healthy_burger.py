from hamburger import Hamburger

class HealthyBurger(Hamburger):
    def __init__(self,__meat, __price):
        self.__name = "Healthy"
        self.__meat = __meat
        self.__price = __price
        self.__bread_roll_type = "White"
        self.__healthy_price = __price

    def add_healthy_addition_1(self, name, price):
        self.__healthy_extra_1_name = name
        self.__healthy_extra_1_price = price
        self.__healthy_price += self.__healthy_extra_1_price
        self.healthy_add_ons = f"Added {self.__healthy_extra_1_name} = ${self.__healthy_extra_1_price}"
        return self.__healthy_price
    
    def add_healthy_addition_2(self, name, price):
        self.__healthy_extra_2_name = name
        self.__healthy_extra_2_price = price
        self.__healthy_price += self.__healthy_extra_2_price
        self.healthy_add_ons += f"\nAdded {self.__healthy_extra_2_name} = ${self.__healthy_extra_2_price}"
        return self.__healthy_price 
    
    def itemize_hamburger(self):
        print(f"{self.__name} Hamburger on {self.__bread_roll_type} with {self.__meat} = ${self.__price}")
        print(f"Your healthy add-ons are: \n{self.healthy_add_ons}")
        return self.__healthy_price
            

print("\n")
healthy_burger = HealthyBurger("Beef", 19.99)
healthy_burger.add_healthy_addition_1("Mustard", .99)
healthy_burger.add_healthy_addition_2("Avocado", 2.50)
print(f"Total Healthy Burger Price is ${str(round(healthy_burger.itemize_hamburger(), 2))}")