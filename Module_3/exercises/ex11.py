# Napisz program, który odczytuje plik tekstowy i zlicza liczbę zdań, słów i znaków w tekście. Wyniki zapisz do pliku CSV.
from collections import Counter


def load_file(file) -> str():
    return file


def count_sentences(file: str()) -> int():
    with open(file) as file:
        file_content = file.read()
        # for line in file_content:
        #     if '.' in line:
        #         cnt +=1
        counter = Counter(file_content)
    return counter['.']


def count_words(file: str()) -> int():
    with open(file) as file:
        file_content = file.read()
        counter = Counter(file_content.split())
        sum = 0

        for cnt in counter.values():
            sum += cnt

        return sum


def count_signs(file: str()) -> int():
    with open(file) as file:
        file_content = file.read()
        counter = Counter(file_content)
        # sum = 0
        return sum(counter.values())


def write_to_csv(sentences: int(), words: int(), signs: int()):
    import csv
    csv_file = '../test_files/test2.csv'
    with open(csv_file, 'w') as file:
        fieldnames = ['sentences', 'words', 'signs']
        csv_writer = csv.DictWriter(file, fieldnames)

        csv_writer.writeheader()
        csv_writer.writerow({'sentences': sentences, 'words': words, 'signs': signs})

if __name__ == "__main__":
    file = load_file('../test_files/test2.txt')

    # print("Liczba zdań: " + str(count_sentences(file)))
    # print("Liczba słów: " + str(count_words(file)))
    # print("Liczba znaków: " + str(count_signs(file)))

    sentences = count_sentences(file)
    words = count_words(file)
    signs = count_signs(file)

    write_to_csv(sentences, words, signs)

