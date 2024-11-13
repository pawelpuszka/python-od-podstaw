# 14. Napisz program, który przypisuje funkcję do zmiennej i wywołuje tę funkcję przez zmienną.

def some_func(name):
    print("Hello " + name)


greet = some_func
greet("Ania")


# 15. Napisz program, który przyjmuje funkcję jako argument i wywołuje ją wewnątrz innej funkcji.

def greetings(func):
    return func


def another_func(func):
    func("Ania")

another_func(some_func)


# 16. Napisz prosty dekorator, który wypisuje komunikat przed i po wywołaniu funkcji.
# 17. Napisz dekorator, który mierzy czas wykonywania funkcji.
# 18. Napisz dekorator, który liczy, ile razy dana funkcja została wywołana.
# 19. Napisz dekorator, który do tekstu zwracanego przez funkcję dodaje dokładną godzinę, w której wywołana została funkcja.