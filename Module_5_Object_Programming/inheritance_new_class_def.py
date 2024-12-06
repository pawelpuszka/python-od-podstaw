class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_description(self):
        print(f'Użytkownik ma na imię {self.name} i ma {self.age} lat.')

    def is_adult(self):
        return self.age >= 18
        
        
class SuperUser(User):
    def __init__(self, name, last_name, age):
        super().__init__(name, age)
        self.last_name = last_name

    def print_another_description(self):
        print(f'Użytkownik ma na imię {self.name} {self.last_name} i ma {self.age} lat.')
    
    def print_description(self):        
        print(f'SuperUser nazywa się {self.name} {self.lastname} i ma {self.age} lat.')
        
        
user = SuperUser('Paweł', 'Kowalski', 42)
# print(user.name)
# print(user.last_name)
# print(user.age)

user.print_description()
user.print_another_description()


