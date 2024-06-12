# lekcja 03.04, 03.05, 03.06, 03.07

# def divide(a, b):
#     return a / b
#
#
# try:
#     a = int(input("Podaj 1szą liczbę: "))
#     b = int(input("Podaj 2gą liczbę: "))
#     print(divide(a, b))
# except ZeroDivisionError:
#     print('Nie można dzielić przez 0')
# except ValueError:
#     print("Podaj liczbę!!")
# finally:
#     print("To wykona się zawsze")


# RZUCANIE WYJĄTKÓW
CURRENT_YEAR = 2024

def calculate_age(year_of_birth):
    if year_of_birth > CURRENT_YEAR:
        # raise Exception("Podany rok jest późniejszy od obecnego")
        raise ValueError("Podany rok jest późniejszy od obecnego")
    return CURRENT_YEAR - year_of_birth


print(calculate_age(2025))
