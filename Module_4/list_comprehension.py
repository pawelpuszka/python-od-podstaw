names = ['Paweł', 'Ania', 'Filip', 'Antek']

names2 = [name for name in names]
# print(names2)

# filtrowanie listy składanej
names3 = [name for name in names if name.endswith('a')]
# print(names3)

# warunkowe tworzenie listy składanej
names4 = [name.upper() if name.endswith('a') else name.lower() for name in names]
# print(names4)

# filtrowanie i warunkowe tworzenie listy
names5 = [name if name.endswith('a') else name.lower for name in names if len(name) <= 4]
# print(names5)

# zapisać dwukrotność liczb 1-10
numbers = [num for num in range(1, 11)]
numbers2 = [num*2 for num in numbers]
# print(numbers2)


# set comprehension
names = ['Paweł', 'Ania', 'Filip', 'Antek', 'Paweł', 'Ania', 'Filip', 'Antek']
names2 = {name for name in names}
# print(names2)


# dictionary comprehension
numbers2 = [pow(num, 2) for num in numbers]
numbers3 = {str(num): num2 for num, num2 in zip(numbers, numbers2)}
print(numbers3)
numbers4 = {num: pow(num, 2) for num in numbers}
print(numbers4)