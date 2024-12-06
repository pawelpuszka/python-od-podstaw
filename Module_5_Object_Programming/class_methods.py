class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def is_adult(self) -> bool:
        return self.age >= 18
    
    def get_description(self):
        print(f'Użytkownik ma na imię {self.name} i ma {self.age} lat.')
    
        
user = User('Paweł', 42)
print(user.is_adult())
user.get_description()
