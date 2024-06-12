# 03.08, 03.09


file_content = None
file = None
try:
    file = open('test_files/test.txt', encoding='utf-8')
    file_content = file.read()
except Exception:
    pass  # zła praktyka!!!!
finally:
    if file is not None:
        file.close()

print(file_content)


with open('test_files/test.txt', encoding='utf-8') as file:
    file_content = file.read()

print(file_content)

# czytanie linia po linii
with open('test_files/test.txt', encoding='utf-8') as file:
    print(file.readline())
    print(file.readline())


with open('test_files/test.txt', encoding='utf-8') as file:
    file_content = file.readlines()  # zraca listę

for line in file_content:
    print(line)


try:
    with open('test_files/test2.txt', encoding='utf-8') as file:
        file_content = file.readlines()  # zwraca listę
        for line in file_content:
            print(line)
except FileNotFoundError:
    print("Nie znaleziono pliku o takiej nazwie")



with open('test_files/test2.txt', encoding='utf-8') as file:
    file_content = file  # czytanie bezpośrednio z dysku,  w przypadku readlines() zawartość pliku ładowana jest do pamięci
    for line in file_content:
        print(line)
