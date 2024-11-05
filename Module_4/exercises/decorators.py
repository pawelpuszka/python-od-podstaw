# 17. Napisz dekorator, który mierzy czas wykonywania funkcji.

def counting(num):
	num = int(num)
	for i in range(1, num+1):
		print(i)


def check_time(func):
	import time
	count_func = func
	start_time = time.time()
	count_func(1_000_000)
	end_time = time.time()
	time_diff = end_time - start_time
	print(time_diff)


# check_time(counting)


# 18. Napisz dekorator, który liczy, ile razy dana funkcja została wywołana.

# def printer():
# 	print("funkcja")
#
#
# def decorator(func):



# 19. Napisz dekorator, który do tekstu zwracanego przez funkcję dodaje dokładną godzinę, w której wywołana została funkcja.




def decorator(func):
	def wrapper():
		from datetime import datetime
		now = datetime.now()
		hour = now.strftime("%H:%M:%S")
		ret_val = func()
		return f"{ret_val}{hour}"
	return wrapper


@decorator
def printer():
	return "Wywołanie o godzinie: "


print(printer())
