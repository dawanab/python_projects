class Person: 
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age
    
    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
    
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
    
    def set_age(self, new_age):
        if new_age < 0 or new_age > 100:
            self.age = 0
        else:
            self.age = new_age

    def is_teen(self):
        if self.age > 12 and self.age < 20:
            return True
        else:
            return False

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return ""
        elif not self.last_name:
            return self.first_name
        elif not self.first_name:
            return self.last_name
        else:
            return self.first_name + " " + self.last_name

my_person = Person("Bergen", "Baka", 3)
my_person.set_age(28)
my_person.set_first_name("Kennedy")
my_person.set_last_name("Baka")

print(my_person.get_age())
print(my_person.get_full_name())
print(my_person.is_teen())

print("\n")

another_person = Person("Harper", "Carlos", 14)
another_person.set_first_name("")
another_person.set_last_name("Alvarez")
print(another_person.get_full_name())
print(another_person.is_teen())
    

         
    

