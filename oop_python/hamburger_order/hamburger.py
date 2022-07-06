class Hamburger:
    def __init__(self, __name, __meat, __price, __bread_roll_type):
        self.__name = __name
        self.__meat = __meat
        self.__price = __price
        self.__bread_roll_type = __bread_roll_type
        self.hamburger_price = __price

    def add_hamburger_addition_1(self, __name, __price):
        self.__addition_1_price = __price
        self.__addition_1_name = __name
        self.hamburger_price += __price
        self.add_ons = f"Added {self.__addition_1_name} = ${self.__addition_1_price}"
        return self.hamburger_price

    def add_hamburger_addition_2(self, __name, __price):
        self.__addition_2_price = __price
        self.__addition_2_name = __name
        self.hamburger_price += __price
        self.add_ons += f"\nAdded {self.__addition_2_name} = ${self.__addition_2_price}"
        return self.hamburger_price


    def add_hamburger_addition_3(self, __name, __price):
        self.__addition_3_price = __price
        self.__addition_3_name = __name
        self.hamburger_price += __price
        self.add_ons += f"\nAdded {self.__addition_3_name} = ${self.__addition_3_price}"
        return self.hamburger_price

    def add_hamburger_addition_4(self, __name, __price):
        self.__addition_4_price = __price
        self.__addition_4_name = __name
        self.hamburger_price += __price
        self.add_ons += f"\nAdded {self.__addition_4_name} = ${self.__addition_4_price}"
        return self.hamburger_price

    def itemize_hamburger(self):
        print(f"{self.__name} Hamburger on {self.__bread_roll_type} with {self.__meat} = ${self.__price}")
        print(f"Your add-ons are: \n{self.add_ons}")
        return self.hamburger_price

hamburger = Hamburger("Basic", "Sausage", 3.56, "White")
hamburger.add_hamburger_addition_1("Tomato", 0.27)
hamburger.add_hamburger_addition_2("Lettuce", 0.75)
hamburger.add_hamburger_addition_3("Cheese", 1.13)
print(f"Total burger price is ${hamburger.itemize_hamburger()}")