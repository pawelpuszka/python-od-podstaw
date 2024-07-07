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


def remove_movie(movie_title):
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        csv_reader = tuple(csv_reader.vales())
        create_library()
        for row in csv_reader:



def get_movie_name_from_user() -> str():
    return input("Tytuł filmu do edycji: ")


def get_movie_from_file(movie_title: str) -> dict():
    with open('data/movies_library.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['title'] == movie_title:
                return row
    raise NameError("Taki film nie istnieje w bazie - dane użytkownika")



def edit_movie(movie: dict, option: int) -> tuple():
    new_movie = movie
    match option:
        case 1:
            new_movie['title'] = input("Podaj nowy tytuł: ")
        case 2:
            new_movie['genre'] = input("Podaj nowy gatunek: ")
        case 3:
            new_movie['year'] = input("Podaj nowy rok premiery: ")

    return tuple(new_movie.values())



if __name__ == "__main__":
    create_library()
    movie = create_movie()
    add_movie(movie)
    movie_title = get_movie_name_from_user()
    movie = get_movie_from_file(movie_title)
    movie = edit_movie(movie, 2)
    print(movie)
