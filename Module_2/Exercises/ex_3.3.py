# Napisz funkcję factorial(n), która przyjmuje liczbę całkowitą n i zwraca jej silnię (n!).

def factorial(number):
    result = 1
    if number > 0:
        result = number * factorial(number - 1)
    return result


print(factorial(10))
