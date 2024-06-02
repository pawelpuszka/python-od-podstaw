# 1. Stwórz listę którą wypełnisz 10 liczbami całkowitymi i zwróć sumę wszytskich liczb z tej listy.

import random

numbers = list()

for i in range(1, 11):
    numbers.append(random.randrange(1, 1000))

sum = 0
for number in numbers:
    print(number)
    sum += number

print(sum)