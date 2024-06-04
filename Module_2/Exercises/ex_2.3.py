# 3. Stwórz listę którą wypełnisz 10 liczbami całkowitymi. Znajdź największą i najmnijeszą liczbę

# ver.1
import random

numbers = list()

for i in range(0, 10):
    numbers.append(random.randrange(1, 100))
    print(numbers[i])

numbers.sort()

print("Biggest number: " + str(numbers[-1]))
print("Smallest number: " + str(numbers[0]))


# ver.2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers[0] >= numbers[1]:
    largest = numbers[0]
    smallest = numbers[1]
else:
    largest = numbers[1]
    smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number

print("Largest number: " + str(largest))
print("Smallest number: " + str(smallest))



