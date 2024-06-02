# 3. Stwórz listę którą wypełnisz 10 liczbami całkowitymi. Znajdź największą i najmnijeszą liczbę

# import random
#
# numbers = list()
#
# for i in range(1, 11):
#     numbers.append(random.randrange(1, 100))
#
# numbers.sort()
#
# print("Biggest number: " + str(numbers[-1]))
# print("Smallest number: " + str(numbers[0]))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if numbers[0] >= numbers[1]:
    biggest = numbers[0]
    smallest = numbers[1]
else:
    biggest = numbers[1]
    smallest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number
    elif number < smallest:
        smallest = number

print("Biggest number: " + str(biggest))
print("Smallest number: " + str(smallest))



