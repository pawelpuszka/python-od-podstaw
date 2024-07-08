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


def show_movies():
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)

        for movie in csv_reader:
            print(f"Tytuł : {movie['title']}")
            print(f"Gatunek: {movie['genre']}")
            print(f"Rok premiery: {movie['year']}")


def _read_movies_from_file_() -> list():
    with open('data/movies_library.csv') as file:
        movies_list = list()
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            movies_list.append(row)
        # print(movies_list)
        return movies_list


def edit_movie(movie: dict, option: int):
    new_movie = movie
    match option:
        case 1:
            new_movie['title'] = input("Podaj nowy tytuł: ")
        case 2:
            new_movie['genre'] = input("Podaj nowy gatunek: ")
        case 3:
            new_movie['year'] = input("Podaj nowy rok premiery: ")

    movies_list = _read_movies_from_file_()

    for movie in movies_list:
        if movie['title'] == new_movie['title']:
            movies_list = new_movie

    with open('data/movies_library.csv') as file:
        csv_writer = csv.writer(file)
        create_library()
        for movie in movies_list:
            add_movie(tuple(movie.values())) !!!!!!!!!!!!!!!!



def remove_movie(movie_title: str):
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        create_library()
        for row in csv_reader:
            if row['title'] != movie_title:
                add_movie(tuple(row.values()))


# def main():
#     while True:
#         option = int(input("Wybierz opcję: "))
#         print("1 - Wyświetl filmy")
#         print("Dodaj nowy film")
#         print("Edytuj film")
#         print("Usuń film")
#         print("Wyszukaj film po tytule")
#
#         match option:
#             case 1:




if __name__ == "__main__":
    create_library()
    movie = create_movie()
    add_movie(movie)
    movie_title = get_movie_name_from_user()
    movie = get_movie_from_file(movie_title)
    edit_movie(movie, 2)
    show_movies()
    # print(movie)
    # print("Usuwanie filmu")
    # movie_title = get_movie_name_from_user()
    # remove_movie(movie_title)
