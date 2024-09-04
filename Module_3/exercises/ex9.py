# 9.Napisz program, który prosi użytkownika o dwie liczby oraz operację (dodawanie, odejmowanie, mnożenie, dzielenie). Obsłuż wyjątki takie jak dzielenie przez zero i nieprawidłowe dane wejściowe.

def get_numbers() -> list():
    try:
        number1 = int(input("Podaj pierwszą liczbę: "))
        number2 = int(input("Podaj drugą liczbę: "))
    except ValueError:
        raise ValueError("Musisz podać liczbę całkowitą")

    return [number1, number2]


def get_operation() -> str():
    op = input("Wybierz operację + - * / :")
    return op


def add(nums: list()):
    return nums[0] + nums[1]


def subtract(nums: list()):
    return nums[0] - nums[1]


def multiply(nums: list()):
    return nums[0] * nums[1]


def divide(nums: list()):
    try:
        result = nums[0] / nums[1]
    except ZeroDivisionError:
        raise ZeroDivisionError("Nie można dzielić przez 0")

    return result


def calculation(nums: list(), operator: str()):
    match operator:
        case '+': return add(nums)
        case '-': return subtract(nums)
        case '*': return multiply(nums)
        case '/': return divide(nums)
        case _: raise ValueError("Nie ma takiego operatora działania")



if __name__ == "__main__":
    nums = get_numbers()
    op = get_operation()
    res = calculation(nums, op)
    print(res)
