# 3.Napisz funkcję, która przyjmuje liczbę jako argument i rzuca wyjątek ValueError jeśli liczba jest ujemna.

def set_number(num):
    if num < 0:
        raise ValueError


try:
    set_number(-1)
except ValueError:
    print("Liczba musi być dodatnia")