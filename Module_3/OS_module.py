import os

path = os.getcwd()
print(path)
print(os.listdir(path))  # wyświetla pliki i foldery bieżącego katalogu

# utworzenie nowego katalogu
new_directory = os.path.join('test_directory')

os.mkdir(new_directory)
print(os.listdir(path))

os.rmdir(new_directory)
print(os.listdir(path))


# czy plik lub folder istnieje
print(os.path.exists('phone-shop'))

print(os.path.isdir('phone-shop'))
print(os.path.isfile('phone-shop'))


# tworzenie pliku w istniejącym katalogu
print(os.getcwd())  #
path = '/home/pawel/PycharmProjects/Python-od-podstaw/Module_3/test_files'

with open(os.path.join('test.py'), 'x'):
    pass

