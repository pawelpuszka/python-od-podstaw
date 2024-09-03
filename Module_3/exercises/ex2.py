# 2.Napisz program, który próbuje odczytać wartość z listy poza jej zakresem i obsłuży wyjątek IndexError.

list = [1, 2, 3]

try:
    for i in range(5):
        print(list[i])
except IndexError:
    print("Za daleko szukasz")
    