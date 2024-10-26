import time




def decorator(func):
	def wrapper():
		print("Przed funkcją")
		func()
		print("Po funkcji")
	return wrapper


def timer(func):
	def wrapper():
		start_time = time.time()
		func()
		end_time = time.time()
		print((end_time - start_time) * 1_000)

	return wrapper

##########################################################
# dekorowanie funkcji poprzez adnotację

@decorator
@timer
def print_func():
	print("Jestem funkcją")


print_func()


# dekorowanie funkcji
# print_func_decorated = timer(decorator(print_func))
#
# print_func_decorated()



