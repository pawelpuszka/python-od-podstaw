with open('test_files/test.txt', 'w+') as file:
    file.write('komputer\n')
    file.write('pies\n')
    file.write('człowiek\n')
    file.seek(0)  # przenosi kursor na początek pliku - 0 do znaku nr 0
    print(file.read())


# 'w+' - umożliwia zapisywanie i odczyt danych w jednym managerze kontekstu
# 'a+' - umożliwia zapisywanie i odczyt danych w jednym managerze kontekstu


with open('test_files/test.txt', 'r+') as file:
    print(file.read())
    file.seek(0, 2)  # przenosi kursor na koniec pliku
    file.write('komputer\n')
    file.write('pies\n')
    file.write('człowiek\n')
    file.seek(0)
    print(file.read())


# 'r+' - umożliwia odczyt ale też zapis danych w jednym managerze kontekstu
#        w tym trybie dane do pliku dopisywane są w miejscu gdzie jest obeznie kursor