import  csv


def _create_header_() -> list():
    return ['title', 'genre', 'year']


def create_library():
    with open('data/movies_library.csv', 'w') as file:
        header = _create_header_()
        csv_writer = csv.DictWriter(file, fieldnames=header)
        csv_writer.writeheader()

def create_movie() -> tuple():
    title = input("Nazwa filmu: ")
    genre = input("Gatunek filmu: ")
    year = input("Rok premiery: ")

    return title, genre, year

def add_movie(movie: tuple):
    title, genre, year = movie
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['title'] == title:
                raise NameError("Taki film już jest w bazie danych - dane użytkownika")
    with open('data/movies_library.csv', 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([title, genre, year])


def get_movie_name_from_user() -> str():
    return input("Podaj tytuł filmu: ")


def get_movie_from_file(movie_title: str) -> dict():
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['title'] == movie_title:
                return row
    raise NameError("Taki film nie istnieje w bazie - dane użytkownika")


def show_movie_info(movie: dict):
    print(f"Tytuł : {movie['title']}")
    print(f"Gatunek: {movie['genre']}")
    print(f"Rok premiery: {movie['year']}")
    print("*******************************")


def show_movies():
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)

        for movie in csv_reader:
            show_movie_info(movie)


def _get_option_value(min: int, max: int) -> int():
    option = int(input("Wybierz opcję: "))
    if (option < min) or (option > max):
        raise ValueError

    return option


def edit_movie(movie: dict, option: int):
    new_movie = movie.copy()
    match option:
        case 1:
            new_movie['title'] = input("Podaj nowy tytuł: ")
        case 2:
            new_movie['genre'] = input("Podaj nowy gatunek: ")
        case 3:
            new_movie['year'] = input("Podaj nowy rok premiery: ")

    remove_movie(movie['title'])
    add_movie(tuple(new_movie.values()))


def remove_movie(movie_title: str):
    movies_list = list()
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movies_list.append(row)

        create_library()
        for row in movies_list:
            if row['title'] != movie_title:
                add_movie(tuple(row.values()))


def _info_(msg: str):
    print()
    print(msg)

def main():
    create_library()

    while True:
        _info_("Menu: ")
        print("1 - Wyświetl filmy")
        print("2 - Dodaj nowy film")
        print("3 - Edytuj film")
        print("4 - Usuń film")
        print("5 - Wyszukaj film po tytule")
        print("0 - Wyjście")

        try:
            option = _get_option_value(0, 5)
        except ValueError:
            print("Musisz podać liczbę od 0 - 5")
            continue

        match option:
            case 1:
                _info_("Lista filmów")
                print("-----------")
                show_movies()
            case 2:
                _info_("Dodawanie nowego filmu")
                movie = create_movie()
                try:
                    add_movie(movie)
                except NameError:
                    print("Taki film już istnieje")
                    continue
            case 3:
                while True:
                    _info_("Edycja filmu")
                    try:
                        movie_title = get_movie_name_from_user()
                        movie = get_movie_from_file(movie_title)
                    except NameError:
                        print("Nie ma takiego filmu w bazie danych")
                        continue
                    print("1 - nazwa")
                    print("2 - gatunek")
                    print("3 - rok premiery")
                    try:
                        option = _get_option_value(1, 3)
                        break
                    except ValueError:
                        print("Musisz podać liczbę 1 - 3")
                        continue
                edit_movie(movie, option)
            case 4:
                _info_("Usuwanie filmu")
                try:
                    movie_title = get_movie_name_from_user()
                    movie = get_movie_from_file(movie_title)
                except NameError:
                    print("Nie ma takiego filmu w bazie danych")
                    continue
                remove_movie(movie_title)
            case 5:
                try:
                    movie_title = get_movie_name_from_user()
                except NameError:
                    print("Nie ma takiego filmu w bazie danych")
                    continue
                movie = get_movie_from_file(movie_title)
                show_movie_info(movie)
            case 0:
                _info_("Koniec programu")
                break


if __name__ == "__main__":
    main()

