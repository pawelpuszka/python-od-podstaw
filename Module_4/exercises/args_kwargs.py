# Napisz funkcję, która przyjmuje dowolną liczbę argumentów liczbowych i zwraca ich sumę.
def sum(*args):
	sum = 0
	for num in args:
		sum += num
	return sum

# print(sum(1, 10, 100, 100))


# Napisz funkcję, która przyjmuje dowolną liczbę argumentów nazwanych i zwraca je jako słownik, w którym klucze posortowane są w kolejności alfabetycznej.

def get_dict(**kwargs):
	ret_val = dict()
	keys = list()
	for key in kwargs.keys():
		keys.append(key)

	keys_sorted = sorted(keys)
	for key in keys_sorted:
		ret_val[key] = kwargs[key]
	return ret_val


# print(get_dict(name="Paweł", age=42, role="DB Developer"))



# Napisz funkcję, która przyjmuje zarówno *args, jak i **kwargs, i wypisuje je.

def print_everyting(*args, **kwargs):
	print(args)
	print(kwargs)


print_everyting("Paweł", "Ania", "Filip", "Antek", name="Ania", age=40, role="wife")