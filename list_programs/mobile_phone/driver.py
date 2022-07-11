from phone import MobilePhone
from contact import Contact

class Driver:

    def __init__(self):
        return self.__print_menu()

    def __print_menu(self):
        print("Select an option: \n")
        print("0 - Shutdown\n" +
            "1 - Print Contacts\n" +
            "2 - Add A New Contact\n" +
            "3- Update An Existing Contact\n" +
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
                return self.add_new_contact()
                
      
my_phone = Driver()

# my_phone = MobilePhone("555 025 0612")
# my_phone._MobilePhone__start_phone()
# my_phone._MobilePhone__print_menu()


""" 
print("0 - Shutdown\n" +
            "1 - Print Contacts\n" +
            "2 - Add A New Contact\n" +
            "3- Update An Existing Contact\n" +
            "4 - Remove An Existing Contact" +
            "5 - Query If An Existing Contact Exists" +
            "6 - View Menu")
             """