# 23.Napisz program, który formatuje bieżącą datę i czas z użyciem f-stringów.
import datetime

now = datetime.datetime
print(f'{now.now():%Y-%m-%d %H:%M:%S}')

# 24.Napisz program, który formatuje liczbę zmiennoprzecinkową do dwóch miejsc po przecinku z użyciem f-stringów.
num = 2.34534243434325678
print(f'{num:.2f}')

# 25.Napisz program, który formatuje liczbę zmiennoprzecinkową jako procent z użyciem f-stringów.
num = 0.78
print(f'{num*100:.0f}%')