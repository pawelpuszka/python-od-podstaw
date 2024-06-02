phone_book = {
     'Filip': 502502502
    ,'Antek': 765987432
    ,'Ania' : 696996696
}

print(phone_book.get('Filip'))  # w przypadku gdy klucz nie istnieje wyrzuca wyjątek KeyError
print(phone_book['Antek'])      # w przypadku gdy klucz nie istnieje zwraca None

phone_book['Paweł'] = 605405756
print(phone_book)

phone_book['Paweł'] = 789456123
print(phone_book)

# usuwanie elementu
del_phone_number = phone_book.pop('Paweł')
print(del_phone_number)
print(phone_book)

# del_phone_number = phone_book.pop('Paweł')  # gdy nie znjadzie klucza - wyjątek KeyError
del_phone_number = phone_book.pop('Paweł', 'Nie znaleziono numeru')
print(del_phone_number)

# wyświetlanie kluczy
for object in phone_book:
    print(object)

# wyświetlanie wartości
for object in phone_book:
    print(phone_book[object])

for object in phone_book.values():
    print(object)

# wyświetlanie par klucz, wartość - metoda zwraca tuple
for object in phone_book.items():
    print(object)

# for object in phone_book.items():
#     print(object[0] + ": " + str(object[1]))

for name, phone_number in phone_book.items():
    print(name + ": " + str(phone_number))