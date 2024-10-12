# Stwórz aplikację, która pozwala użytkownikom tworzyć, usuwać i aktualizować zadania. Zadania powinny być przechowywane w pliku JSON.
# Każde zadanie powinno mieć tytuł, opis i status (np. “do zrobienia”, “w trakcie”, “zrobione”).


def create_file(file_name: str()):
    from pathlib import Path
    Path(fr'../test_files/{file_name}').touch(exist_ok=True)


def create_task() -> str():
    return input("Podaj nazwę zadania: ")


if __name__ == "__main__":
    create_file('tasks.json')


