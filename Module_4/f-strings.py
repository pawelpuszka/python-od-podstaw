name = 'Paweł'

print("Cześć " + name + "!")
print("Cześć %s" % name)
print("Cześć {}!".format(name))
print(f"Cześć {name}")

print(f"Cześć {name.upper()}")

# instrukcje warunkowe w f-string
name = 'Ania'
print(f"Gratulacje, {'wygrałaś' if name.endswith('a') else 'wygrałeś'}")


# Operacje liczbowe i formatowanie liczb z użyciem f-stringa
print(f"wynik dodawania to {2 +7}")

num = 2.149878937
print(f'{num:.4f}')  # 2f określa ile liczb po przecinku
num = 2149878937
print(f'{num:,}')
print(f'{num:_}')
num = 2149878937.765658767
print(f'{num:_.3f}')


# Formatowanie dat z użyciem f-stringa
import datetime

now = datetime.datetime
# print(f'{now:%Y-%m-%d}')


# Wyrównywanie tekstu w konsoli z użyciem f-stringa
users = {
	'Pawel': 42,
	'Ania': 40,
	'Filip': 14,
	'Antek': 4
}

for name, age in users.items():
	print(f'{name:10} {age}')

for name, age in users.items():
	print(f'{name:>10} {age}')  # wyrównanie do prawej

for name, age in users.items():
	print(f'{name:^10} {age}')  # wyśrodkowanie

for name, age in users.items():
	print(f'{name:_^10} {age}')  # wyśrodkowanie ze wypełnieniem


# wyświetlanie znawy zmiennej wraz z jej wartością - np przy debugowaniu
name = 'Paweł'
print(f'{name=}')