class User:
    def __init__(self, name: str, mail: str, age: int):
        self.name = name
        self.mail = mail
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.mail)
        print(self.age)

    def is_male(self):
        return not self.name.endswith('a')
        # return self.name[-1] != 'a'

user = User('Paweł', 'pawel.puszka@gmail.com', 42)
user.print_info()
print(user.is_male())

