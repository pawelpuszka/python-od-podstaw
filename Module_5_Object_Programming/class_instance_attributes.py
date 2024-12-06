class User:
    company = 'Sorigo'  # atrybuty klasy który jest wspolny dla wszystkich instancji
    def __init__(self, name, age):  # atrybuty instancji
        self.name = name
        self.age = age
        

user = User('Paweł', 42)
print(user.company)
print(user.name)
print(user.age)

user1 = User('Ania', 40)
print(user1.company)
print(user1.name)
print(user1.age)

print(User.company)

User.company = 'Google'
print(user.company)
