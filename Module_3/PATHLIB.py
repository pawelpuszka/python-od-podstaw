from pathlib import Path

current_directory = Path.cwd()
print(current_directory)

# co znajduje się w katalogu
for item in current_directory.iterdir():
    print(f'{item} {item.is_file()} {item.is_dir()}')

# tworzenie katalogiu
Path('test_dir').mkdir(exist_ok=True)  # nie rzuci wyjątku gdy katalog już istnieje

current_directory = Path.cwd()
Path(fr'{current_directory}\test\test_dir').mkdir(parents=True, exist_ok=True)

# utworzenie nowego pliku
new_file = 'file.txt'
Path(fr'{current_directory}\test\test_dir\{new_file}').touch()
