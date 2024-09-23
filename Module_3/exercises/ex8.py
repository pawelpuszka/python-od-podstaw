# Napisz program, który mierzy czas wykonywania funkcji obliczającej sumę liczb od 1 do 1,000,000.

import time
# from datetime

def get_time():
    print(time.time() / 60)
    return time.time()


def count(start: int(), stop: int()):
    for i in range(start, stop+1):
        pass


def print_result(start, end):
    print(end - start)


if __name__ == "__main__":
    start = get_time()
    count(1, 1000000)
    end = get_time()
    print_result(start, end)
