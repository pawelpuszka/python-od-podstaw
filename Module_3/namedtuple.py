from collections import namedtuple

# person = ('Paweł', 42)
# print(person[0])

Person = namedtuple('Person', ['name', 'age'])
person = Person(name='Paweł', age=36)

print(person.age)
print(person[0])

