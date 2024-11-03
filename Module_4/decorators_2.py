# Przekazywanie funkcji jako argument do innej funkcji
def get_hello(hello_function):
	def hello(name):
		hello_function(name)

	return hello

def english_hello(name):
	print(f'Hello {name}!')
def polish_hello(name):
	print(f'Cześć {name}')


# hello = get_hello(english_hello)
# hello("Paweł")


# Dekorowanie funkcji
def print_func():
	print("Jestem funkcją")


def decorator(func):
	print("Przed funkcją")
	func()
	print("Po funkcji")


# decorator(print_func)

# dekorowanie funkcji - licznik czasu
import time

def timer(func):
	start_time = time.time()
	func()
	end_time = time.time()
	print((end_time - start_time) * 1_000)


timer(print_func)


