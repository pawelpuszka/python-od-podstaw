# Napisz program, który listuje wszystkie pliki w danym folderze oraz ich rozmiary, korzystając z modułu pathlib.

from pathlib import Path

def get_directory() -> str():
    dir = input("Podaj ścieżkę do katalogu: ")
    if dir is None:
        dir = Path.cwd()
    return Path(dir)
    # dir = Path(dir)
    # for folder in dir.iterdir():
    #     folder


def get_folders_list(dir):
    for folder in dir.iterdir():
        print(f'{folder}    {round((folder.stat().st_size / 1024), 2)}kB')


if __name__ == "__main__":
    dir = get_directory()
    get_folders_list(dir)
