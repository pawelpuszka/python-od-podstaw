class Human:

    def __init__(self, name, language):
        self.name = name
        self.language = language
        
        
    def speak(self):
        if self.language == 'pl':
            print(f'Czesć mam na imię {self.name}' )
        elif self.language == 'en':
            print(f'Hello, my name is {self.name}')
            
            
class Dog:
    def __init__(self, language):
        self.language = language
        
    def bark(self):
        if self.language == 'pl':
            print('Hau hau')
        elif self.language == 'en':
            print('Woof woof')
            
            
class Mutant(Human, Dog):
    def __init__(self, name, language):
        Human.__init__(self, name, language)
        Dog.__init__(self, language)
        
        
mutant = Mutant('Dogmeat', 'pl')
mutant.bark()
mutant.speak()