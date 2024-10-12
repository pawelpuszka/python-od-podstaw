# Napisz program, który pozwala użytkownikowi dodawać pozycje do listy zakupów i zapisuje tę listę do pliku tekstowego.


def get_list_name() -> str():
    return input("Podaj nazwę swojej listy: ")


def create_list(list_name: str()) -> str():
    from pathlib import Path
    list_file = list_name + '.txt'
    file_dir = fr'..\test_files\{list_file}'
    Path(file_dir).touch(exist_ok=True)
    return file_dir



def get_item() -> str():
    return input("Podaj składnik listy: ")




def add_item_to_file(item, file):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(item + '\n')



if __name__ == "__main__":
    list_name = get_list_name()
    file = create_list(list_name)

    while True:
        item = get_item()
        add_item_to_file(item, file)
        if input("Czy chcesz dodać kolejny składnik (t/n) ? ") == 'n':
            break
