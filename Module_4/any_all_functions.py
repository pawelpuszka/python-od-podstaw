# all - zwraca True jeżeli każde wyrażenie z przekazanej listy/obiektu zwraca True
# any - zwraca True jeżeli chociaż jedno wyrażenie z przekazanej listy/obiektu zwraca True

values = [True, True, True]

print(all(values))
print(any(values))


values = [True, True, False]

print(all(values))
print(any(values))

names = ['Paweł', 'Ania', 'Filip', 'Antek']
names2 = [name.endswith('a') for name in names]
print(names2)
print(all(names2))
print(any(names2))