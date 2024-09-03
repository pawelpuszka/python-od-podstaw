# 5.Napisz program, który prosi użytkownika o podanie kilku imion i zapisuje je do pliku tekstowego.

def create_new_file(file_name: str()):
    from pathlib import Path
    Path(f"../test_files/{file_name}").touch()


def get_name() -> str():
    name = input("Podaj imię: ")
    return name


def write_to_file(name: str()):
    with open('../test_files/names', 'a') as file:
        name_with_nl = f"{name}\n"
        file.write(name_with_nl)


def print_file():
    with open('../test_files/names') as file:
        file_content = file.read()

        print(file_content)


if __name__ == "__main__":
    create_new_file('names')
    name1 = get_name()
    write_to_file(name1)
    name2 = get_name()
    write_to_file(name2)
    name3 = get_name()
    write_to_file(name3)

    print_file()






