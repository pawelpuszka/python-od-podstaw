# 1.Napisz program, który próbuje podzielić liczbę przez zero i obsłuży wyjątek ZeroDivisionError.

try:
    a = 3 / 0
except ZeroDivisionError:
    print('Pamiętaj cholero nie dziel przez zero')