# Napisz program, który wczytuje plik tekstowy i pozwala użytkownikowi wyszukiwać słowa. Program powinien wypisywać wszystkie linie, w których występuje wyszukiwane słowo.

def load_file(file) -> str():
    return file


def get_word() -> str():
    word = input("Podaj wyszukiwane słowo ")
    return word


def find_lines(word, file):
    with open(file) as file:
        file_content = file
        for line in file_content:
            if word in line:
                print(line)


if __name__ == "__main__":
    file = load_file('../test_files/test2.txt')
    while True:
        word = get_word()
        find_lines(word, file)
        if input("Kontynuować program (y/n)? ") == 'n':
            break