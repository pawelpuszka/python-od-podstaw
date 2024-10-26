# Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia długości listy.

print(len(squares_list := [x**2 for x in range(1, 11)]))
print(squares_list)


# Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia, czy liczba jest parzysta.

def is_even(num) -> bool:
	return num % 2 == 0


print(val := is_even(5))
print(val)


# Napisz program, który używa operatora walrus do jednoczesnego przypisania i sprawdzenia, czy wpisana przez użytkownika liczba jest dodatnia.

if num := int(input("Podaj liczbę ")) > 0:
	print("Dodatnia")
else:
	print("Ujemna")