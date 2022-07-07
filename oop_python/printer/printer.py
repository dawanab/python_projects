class Printer:
    def __init__(self, __toner_level, __duplex):
        self.__pages_printed = 0
        self.__duplex = __duplex
        if __toner_level > -1 and __toner_level <= 100:
            self.__toner_level = __toner_level
        else:
            self.__toner_level = -1

    def add_toner(self, __toner_amount):
        if __toner_amount > 0 and __toner_amount <= 100:
            self.__toner_amount = __toner_amount
            if self.__toner_amount + self.__toner_level > 100:
                return -1
            self.__toner_level += __toner_amount
        else:
            return -1
        return self.__toner_level

    def print_pages(self, __pages):
        self.__pages_to_print = __pages
        if self.__duplex is True:
            self.__pages_to_print = int((__pages / 2) + (__pages % 2))
        else:
            self.__pages_to_print = __pages
        self.__pages_printed += self.__pages_to_print
        self.__toner_level -= 10
        return f"Printing {self.__pages_to_print} pages..."

    def get_pages_printed(self):
        return f"Number of pages printed = {self.__pages_printed}"

    def get_toner_level(self):
        return self.__toner_level

# Creating a Printer object: 
printer = Printer(100, True)
# Verifying amount of toner:
print(f"Your current toner level = {printer.get_toner_level()}")
# Printing on my duplex:
print(printer.print_pages(10))
# Verifying toner level again
print(f"Your current toner level = {printer.get_toner_level()}")
# Getting number of pages printed:
print(printer.get_pages_printed())


print("\n======")
non_duplex = Printer(100, False)
print(f"Your current toner level = {non_duplex.get_toner_level()}")
print(non_duplex.print_pages(10))
print(f"Your current toner level = {non_duplex.get_toner_level()}")
print(non_duplex.get_pages_printed())
print(non_duplex.print_pages(10))
print(non_duplex.get_pages_printed())
print(f"Your current toner level = {non_duplex.get_toner_level()}")
