class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Paweł', 42)
user1 = User('Ania', 40)

print(user)
print(user.name)
print(user.age)

print(user)
print(user1.name)
print(user1.age)