class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        if name.endswith('a'):
            self._gender = 'female'
        else:
            self._gender = 'male'
            
    def is_male(self):
        return self._gender == 'male'
    
            
            
user = User('Paweł', 42)
print(user.name)
print(user._gender)  # nie powinno byc dostepne, nie wykorzystujemy prywatnych atrybutów w taki sposób
print(user.is_male())
        
        
        
class User2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._gender = self._determine_gender()
        
    def _determine_gender(self):
        return 'female' if self.name.endswith('a') else 'male'
            
    def is_male(self):
        return self._gender == 'male'
        
        
user = User2('Paweł', 42)
print(user.name)
print(user.is_male())
    