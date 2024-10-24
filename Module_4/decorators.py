# 04.10
def hello():
	print("hello!")

greeting = hello  # przypisanie funkcji hello do zmiennej greeting; brak nawiasów - brak wywołania funkcji

print(type(greeting))

# wywołanie funkcji hello() na dwa sposoby
hello()
greeting()

#  funkcja z parametrami
def hello(name):
	print("hello " + name + "!")

greeting = hello
greeting('Paweł')


# 04.12
# funkcja wewnątrz funkcji; funkcja nadrzędna zwraca funkcję wewnętrzną w zależności od spełnionych warunków
def get_hello(language):
	def english_hello(name):
		print(f'Hello {name}!')
	def polish_hello(name):
		print(f'Cześć {name}')

	if language == 'pl':
		return polish_hello
	elif language == 'en':
		return english_hello


greeting = get_hello('en')
greeting('Paweł')




