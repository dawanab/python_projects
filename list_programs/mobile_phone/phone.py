class MobilePhone:

    def __init__(self, __my_number):
        self.__my_number = __my_number
        self.my_contacts = []
        return self.print_menu()

    # Add a new contact to the mobilePhone
    def add_new_contact(self):
        __contact = input("Please enter the name of your contact: " )
        if __contact in self.my_contacts:
            print(f"{__contact} is already in your phone.")
            return False
        else:
            self.my_contacts.append(__contact)
            print(self.my_contacts)
            return True 
    
    # Update an existing contanct's information
    def update_contact(self, __old_contact, __new_contact):
        found_position = self.__find_contact(__old_contact)
        if found_position < 0:
            print(f"{__old_contact.get_name()} was not found.")
            return False
        elif self.__find_contact(__new_contact.get_name() != -1):
            print(f"Contact: {__new_contact.get_name()} already exists. Update not successful.")
            return False
        else:
            for i in range(len(self.my_contacts)):
                if found_position in self.my_contacts:
                    found_position = self.__new_contact
                    print(f"{__old_contact.get_name()} was replaced with {__new_contact.get_name()}")
                    return True 
                

    # # Search for a contact that is in the contact list
    def __find_contact_by_index(self, contact):
        return self.my_contacts.index(contact)
    
    def __find_contact(self, contact_name):
        for i in range(len(self.my_contacts)):
            contact = self.my_contacts.index(i)
            if contact.get_name() == contact_name:
                return i
        return -1

    # Remove a contact
    def remove_contact(self, contact):
        __found_position = self.__find_contact(contact)
        if __found_position < 0:
            print(f"{contact.get_name()}, was not found.")
            return False
        else:
            self.my_contacts.remove(__found_position)
            print(f"{contact.get_name()}, was deleted.")
            return True 

    # Query a contact by contact in phone
    def query_contact(self, contact):
        if self.__find_contact(contact) >= 0:
            return contact.get_name()
        return None 

    # Query a contact by name
    def query_contact(self, name):
        position = self.__find_contact_by_index(name)
        if position >= 0:
            return self.my_contacts.index(position)
        return None

    # Print contacts
    def print_contacts(self):
        print("Contact List:")
        for i in range(len(self.my_contacts)):
            print(f"{i + 1}. {self.my_contacts.index(i).get_name()} = {self.my_contacts.index(i).get_phone_number()}")

    """ Starting a method with a dunder causes Python to do name mangling.
    Because of this, we call private methods such: object.Class_Name.method_to_call() """
    def __start_phone(self):
        print("Phone is booting up!")

    # def __print_menu(self):
    #     print("Select an option: \n")
    #     print("0 - Shutdown\n" +
    #         "1 - Print Contacts\n" +
    #         "2 - Add A New Contact\n" +
    #         "3- Update An Existing Contact\n" +
    #         "4 - Remove An Existing Contact\n" +
    #         "5 - Query If An Existing Contact Exists\n" +
    #         "6 - View Menu")
    #     print("Please select an option.")

    def print_menu(self):
        print("Select an option: \n")
        print("0 - Shutdown\n" +
            "1 - Print Contacts\n" +
            "2 - Add A New Contact\n" +
            "3 - Update An Existing Contact\n" +
            "4 - Remove An Existing Contact\n" +
            "5 - Query If An Existing Contact Exists\n" +
            "6 - View Menu")
        print("Please select an option.")

        quit = False
        while quit != True:
            option = input("Enter an option: (6 available options)" )
            if option == "0":
                print("\nShutting down...")
                quit = True
                break
            elif option == "1":
                self.print_contacts()
                break
            elif option == "2":
                self.add_new_contact() # Come back and fix this


my_phone = MobilePhone("555 025 0612")

        

    
    
    
    
