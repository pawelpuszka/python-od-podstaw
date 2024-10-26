# 1.Napisz program, który tworzy listę kwadratów liczb od 1 do 10 z użyciem list comprehension.

squares_list = [x**2 for x in range(1, 11)]
print(squares_list)
print(squares_list := [x**2 for x in range(1, 11)])
print(squares_list)


# 2. Napisz program, który tworzy listę liczb parzystych od 1 do 20 z użyciem list comprehension.

even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)


# 3. Napisz program, który tworzy listę, która zawiera "parzysta" lub "nieparzysta" dla liczb od 1 do 10 z użyciem list comprehension.

even_numbers = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in range(1, 21)]
print(even_numbers)


# 4. Napisz program, który tworzy listę, gdzie liczby z zakresu 1-10 są podwojone jeśli są parzyste, a potrojone jeśli są nieparzyste, z użyciem list comprehension.

numbers = [x*2 if x % 2 == 0 else x*3 for x in range(1, 11)]
print(numbers)


# 5. Napisz program, który tworzy listę pierwszych liter każdego słowa w podanym zdaniu z użyciem list comprehension.

sentence = "Ala ma kota"
letters = [x[0] for x in sentence.split()]
print(letters)


# 6. Napisz program, który tworzy zbiór unikalnych znaków z podanego słowa z użyciem set comprehension.

sentence = "Ala ma kota"
letters = {x for x in sentence.strip()}
print(letters)


# 7. Napisz program, który tworzy słownik, gdzie kluczami są liczby od 1 do 5, a wartościami ich kwadraty z użyciem dictionary comprehension.

numbers = {x: x**2 for x in range(1, 6)}
print(numbers[5])


# 8. Napisz program, który tworzy słownik z liczbami od 1 do 10 jako kluczami i ich kwadratami jako wartościami, ale tylko dla liczb parzystych, z użyciem dictionary comprehension.

numbers = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(numbers)