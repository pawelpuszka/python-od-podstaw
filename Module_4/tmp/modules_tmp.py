a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))

import calculator as calc

# from calculator import add 
# from calculator import *  # importuj wszystko z modulu calculator
print(calc.add(a, b))
print(calc.sub(a, b))
print(calc.mul(a, b))
print(calc.div(a, b))

