class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        def get_description(self):
            print(f'Użytkownik ma na imię {self.name} i ma {self.age} lat.')
            
        def is_adult(self):
            return self.age >= 18
        
        
class SuperUser(User):
    pass



user = SuperUser('Paweł', 42)
print(user.name)
print(user.age)
