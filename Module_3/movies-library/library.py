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


def get_movie_name() -> str():
    return input("Tytuł filmu do edycji: ")

def edit_movie(movie_name: str):



if __name__ == "__main__":
    create_library()
    movie = create_movie()
    add_movie(movie)