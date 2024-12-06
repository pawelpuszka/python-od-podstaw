class User:  # tak w Pythonie się nie robi
    def __init__(self, name, age):
        self._name = name.upper()
        self._age = age
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self, name):
        self._name = name.upper()
        
    def set_age(self, age):
        if self._age < 0 or self.age > 130:
            raise ValueError
        self._age = age
        
        
        
# user = User('Paweł', 42)
# print(f'{user.name} {user.age}')



class User2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.upper()
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age < 0 or age > 130:
            raise ValueError
        self._age = age
        
        
        
user = User2('Paweł', -42)
print(f'{user.name} {user.age}')