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
        print(f"You have {len(self.grocery_list)} items in your grocery list.")
        for grocery in self.grocery_list:
            num += 1
            print(f"{num}. {grocery}")
        print(self.grocery_list)

    # Modify the grocery list
    def modify_grocery_item(self, current_item, new_item):
        self.position = self.find_item(current_item)
        if self.position >= 0:
            self.modify_grocery_item_by_position(self.position, new_item)
        return self.grocery_list

    def modify_grocery_item_by_position(self, position, new_item):
        self.item_to_remove = self.grocery_list[position]
        self.grocery_list[position] = new_item
        print(f"Grocery Item {position + 1} ({self.item_to_remove}) has been modified...")
        return self.grocery_list

    # Verify that a particular item is in the list 
    def find_item(self, search_item):
        if search_item in self.grocery_list:
            return self.grocery_list.index(search_item)
        else:
            return "Sorry, that item is not in your grocery list."

    # Remove an item from the list 
    def remove_grocery_item(self, item):
        if item in self.grocery_list:
            self.grocery_list.remove(item)
            print(f"Now removing {item} from your list...")
        return self.grocery_list

   
    # Is item on file method
    def on_file(self, search_item):
        if search_item in self.grocery_list:
            return True
        return False

my_grocery = Grocery()
my_grocery.get_grocery_list()
# Adding items to the grocery list
my_grocery.add_grocery_item("Milk")
my_grocery.add_grocery_item("Eggs")
print("Printing out the grocery list: ")
my_grocery.print_grocery_list()

print("\nget_grocery_list() --->")
print(my_grocery.get_grocery_list())

# Modifying the grocery list
print("\nmodify_grocery_list() --->")
print(my_grocery.modify_grocery_item("Milk", "Cheese"))

my_grocery.add_grocery_item("Pancakes")

# Finding a specific item
print("\nfind_item() --->")
print(my_grocery.find_item("Mash"))
print(my_grocery.find_item("Pancakes"))

# Removing a grocery item
print(my_grocery.remove_grocery_item("Cheese"))

# Printing the grocery list 
my_grocery.print_grocery_list()







    

    
