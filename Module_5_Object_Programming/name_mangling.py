class User2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__gender = self.__determine_gender()
        
    def __determine_gender(self):
        return 'female' if self.name.endswith('a') else 'male'
            
    def is_male(self):
        return self.__gender == 'male'
        
        
user = User2('Paweł', 42)
print(user.name)
print(user.is_male())
print(user._User2__gender)