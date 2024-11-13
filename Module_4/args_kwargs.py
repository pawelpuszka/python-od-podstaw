# *args - dowolna liczba argumentów pozycyjnych, tuple

def print_names(*args):
	for arg in args:
		print(arg)


# print_names("Paweł", "Ania", "Filip", "Antek")




names = ["Antek", "Filip"]

def print_names(names_list: list, *args):
	for arg in args:
		names_list.append(arg)


print_names(names, "Ania", "Paweł")
# print(names)



# *kwargs - dowolna liczba argumentów nazwanych, słownik
# można dodawać argumenty nazwane przed kwargs

def save_user_info(**kwargs):
	user_info = dict()

	for key, value in kwargs.items():
		user_info[key] = value

	return user_info


user = save_user_info(name="Paweł", age=42)
# print(user)



# args i kwargs w jednej funkcji
# *args umieszcza się po argumnetach pozycyjnych
def save_user_info(*skills, **details):
	user_info = dict()

	for key, value in details.items():
		user_info[key] = value

	user_info['skills'] = skills

	return user_info

user = save_user_info('Java', 'Python', 'PLSQL', name="Paweł", age=42)
print(user)