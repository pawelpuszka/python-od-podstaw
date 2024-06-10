import random

number = random.randint(0, 100)

while True:
    user_num = int(input("Zgaduj liczbę "))

    if user_num == number:
        print("Odgadłeś liczbę")
        break

    if user_num > number:
        print("Podałeś za dużą liczbę")
        continue

    if user_num < number:
        print("Podałeś za małą liczbę")