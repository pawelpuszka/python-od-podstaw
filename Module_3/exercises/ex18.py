# Napisz aplikację, która zawiera pytania z różnych kategorii wraz z czterema odpowiedziami, z czego tylko jedna jest poprawna.
# Pytania i odpowiedzi powinny być przechowywane w pliku JSON. Użytkownik powinien móc wybierać kategorię, odpowiadać na pytania i otrzymywać wynik na końcu.

import json

# API

def get_quiz():
    with open('../test_files/quiz_questions.json', 'r') as file:
        questions = json.load(file)
    return questions


def get_elements_count() -> int:
    quiz = get_quiz()
    return len(quiz)


def get_categories() -> list:
    quiz = get_quiz()
    categories = [element["category"] for element in quiz]
    return categories


def get_question(category: str) -> str:
    quiz = get_quiz()
    questions = [element["question"] for elemnt in quiz if elemnt["category"] == category]




# UI

def ui_display_categories(categories: list):
    for id, category in enumerate(categories):
        print(f"{id+1} {category}")
def ui_select_option(max) -> str:
    try:
        option = int(input("Wybierz opcję "))
    except TypeError:
        raise TypeError("Wartość nie może być stringiem. Podaj liczbę od 1 do " + str(max))
    if  option < 1 or option > max:
        raise ValueError("Wartość poza zakresem. Podaj liczbę od 1 do " + str(max))

    return option





if __name__ == "__main__":
    categories = get_categories()
    ui_display_categories(categories)
    max = get_elements_count()
    print("max " + str(max))
    option = ui_select_option(max)
    print(option)
