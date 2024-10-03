print(a := 2)  # walrus operator
print(a == 2)

import random

numbers = [random.randint(1, 10) for _ in range(10)]
# print(numbers)

numbers = [num for _ in range(10) if (num := random.randint(1, 10)) > 5]
# print(numbers)



############################
expenses = []

while (expense := int(input("Podaj wydatek "))) > 0:
    expenses.append(expense)

print(sum(expenses))