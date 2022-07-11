from phone import MobilePhone

class Contact:
    
    def __init__(self, __name, __phone_number):
        self.__name = __name
        self.__phone_number = __phone_number

    def get_name(self):
        return self.__name
    
    def get_phone_number(self):
        return self.__phone_number
    
    def create_new_contact(self, __name, __phone_number):
        return Contact(self, __name, __phone_number)