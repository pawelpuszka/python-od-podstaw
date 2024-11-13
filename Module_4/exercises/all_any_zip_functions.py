# 28. Napisz program, który używa funkcji all i any do sprawdzenia, czy wszystkie lub niektóre elementy listy spełniają określony warunek.
def is_greater_then_10(num: int) -> bool:
    return num > 10


print(any([is_greater_then_10(11), is_greater_then_10(100), is_greater_then_10(8)]))
print((all([is_greater_then_10(1), is_greater_then_10(10), is_greater_then_10(100)])))


# 29. Napisz program, który łączy dwie listy (np. imiona i nazwiska) w jedną listę krotek z użyciem zip.
names = ['Paweł', 'Ania', 'Filip', 'Antek']
surnames = ['Puszka']

from itertools import cycle

family = (list(zip(names, cycle(surnames))))
print(family)



# 30. Napisz funkcję, która zwraca inną funkcję jako wynik. Wywołaj zwróconą funkcję.
def decorator():
    def is_greater_then_10(num: int) -> bool:
        return num > 10

    return is_greater_then_10

val = decorator()
print(val(10))


# 31. Napisz funkcję, która zwraca funkcję do mnożenia podanej liczby przez inną liczbę.

def decorator():
    def multiply_by_10(num):
        return num * 10

    return multiply_by_10


func = decorator()

print(func(10))
