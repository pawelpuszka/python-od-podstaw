# Napisz program, który generuje losowe hasła o zadanej długości, zawierające litery, cyfry i znaki specjalne. Wygenerowane hasła zapisz do pliku tekstowego.

import random
import string

characters = string.ascii_letters
# print(type(characters))
digits = string.digits
# print(type(digits))


length = 100
sequence = list()

while length > 0:
    choice = random.randint(0, 1)
    if choice == 0:
        sequence.append(random.choice(characters))
    else :
        sequence.append(random.choice(digits))
    length -= 1

sequence_str = ''.join(sequence)
with open('../test_files/test.txt', 'a') as file:
    file.write(sequence_str + '\n')
