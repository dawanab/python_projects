from hamburger import Hamburger

class DeluxeBurger(Hamburger):
    def __init__(self):
        super().__init__("Deluxe", "Fully Cooked", 14.54, "Wheat")
        super().add_hamburger_addition_1("Chips", 2.50)
        super().add_hamburger_addition_2("Drink", 1.80)


    def add_hamburger_addition_1(self, __name, __price):
        print(f"Sorry. Can't add additional items to a deluxe burger.")
    
    def add_hamburger_addition_2(self, __name, __price):
        print(f"Sorry. Can't add additional items to a deluxe burger.")
    
    def add_hamburger_addition_3(self, __name, __price):
        print(f"Sorry. Can't add additional items to a deluxe burger.")

    def add_hamburger_addition_4(self, __name, __price):
        print(f"Sorry. Can't add additional items to a deluxe burger.")



