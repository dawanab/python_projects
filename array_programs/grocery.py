

class Grocery:
  
    def __init__(self, grocery_list = []):
        self.grocery_list = grocery_list

    # Add an item to the grocery_list array
    def add_grocery_item(self, item):
        self.grocery_list.append(item)

        

    # Return the items that were added to the gorcery_list
    def get_grocery_list(self):
        return self.grocery_list
    
    # Print the grocery list
    def print_grocery_list(self):
        num = 0
        for grocery in self.grocery_list:
            num += 1
            print(f"{num}: {grocery}")
        return self.grocery_list



my_grocery = Grocery()
my_grocery.get_grocery_list()
my_grocery.add_grocery_item("Milk")
my_grocery.add_grocery_item("Eggs")
my_grocery.print_grocery_list()
print(my_grocery.get_grocery_list())

    

    
