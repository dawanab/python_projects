from unicodedata import name


class Hamburger:
    def __init__(self, __name, __meat, __price, __bread_roll_type):
        self.__name = __name
        self.__meat = __meat
        self.__price = __price
        self.__bread_roll_type = __bread_roll_type

    def add_hamburger_addition_1(self, __name, __price):
        self.__addition_1_price = __price
        self.__addition_1_name = __name

    def add_hamburger_addition_2(self, __name, __price):
        self.__addition_2_price = __price
        self.__addition_2_name = __name

    def add_hamburger_addition_3(self, __name, __price):
        self.__addition_3_price = __price
        self.__addition_3_name = __name

    def add_hamburger_addition_4(self, __name, __price):
        self.__addition_4_price = __price
        self.__addition_4_name = __name

    def itemize_hamburger(self):
        hamburger_price = self.__price
        print(f"{self.__name} hamburger on {self.__bread_roll_type} with {self.__meat} = ${self.__price}")
        if self.__addition_1_name is not None:
            hamburger_price += self.__addition_1_price
            print(f"Added {self.__addition_1_name} = ${self.__addition_1_price}")
        else:
            return hamburger_price

        if self.__addition_2_name is not None:
            hamburger_price += self.__addition_2_price
            print(f"Added {self.__addition_2_name} = ${self.__addition_2_price}")
        else:
            return hamburger_price

        if self.__addition_3_name is not None:
            hamburger_price += self.__addition_3_price
            print(f"Added {self.__addition_3_name} = ${self.__addition_3_price}")
        else:
            return hamburger_price

        if self.__addition_4_name != None:
            hamburger_price += self.__addition_4_price
            print(f"Added {self.__addition_4_name} = ${self.__addition_4_price}")
        else:
            return hamburger_price
    
        return hamburger_price

# hamburger = Hamburger("Basic", "Sausage", 3.56, "White")
# hamburger.add_hamburger_addition_1("Tomato", 0.27)
# hamburger.add_hamburger_addition_2("Lettuce", 0.75)
# hamburger.add_hamburger_addition_3("Cheese", 1.13)
# hamburger.add_hamburger_addition_4("Mayonaise", 0.25)
# print(f"Total burger price is ${ hamburger.itemize_hamburger()}")