class MobilePhone:

    def __init__(self, __my_number):
        self.__my_number = __my_number
        self.my_contacts = []

    # Add a new contact to the mobilePhone
    def add_new_contact(self, __contact):
        if __contact in self.my_contacts:
            print(f"{__contact} is already in your phone.")
        self.my_contacts.append(__contact)
        return True 
    
    # Update an existing contanct's information
    def update_contact(self, __old_contact, __new_contact):
        
