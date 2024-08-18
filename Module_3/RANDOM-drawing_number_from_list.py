import random

numbers = [1, 2, 5, 75, 89, 90, 333, 341, 674, 3, 9, 77, 53, 0, 800]

length = len(numbers)
index = random.randint(0, length-1)

print(index)
print(numbers[index])

print(random.choice(numbers))
print(random.choices(numbers, k=2, weights=[2, 1, 1, 2, 10, 1, 1, 1, 2, 1, 1, 3, 2, 1, 1]))
print(random.sample(numbers, 2))

print()
print(numbers)
random.shuffle(numbers)
print(numbers)