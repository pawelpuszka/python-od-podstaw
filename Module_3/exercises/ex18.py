# Napisz aplikację, która zawiera pytania z różnych kategorii wraz z czterema odpowiedziami, z czego tylko jedna jest poprawna.
# Pytania i odpowiedzi powinny być przechowywane w pliku JSON. Użytkownik powinien móc wybierać kategorię, odpowiadać na pytania i otrzymywać wynik na końcu.

import json

# API

def _get_quiz():
    with open('../test_files/quiz_questions.json', 'r') as file:
        questions = json.load(file)
    return questions


def get_elements_count() -> int:
    quiz = _get_quiz()
    return len(quiz)


def _get_all_categories() -> list:
    quiz = _get_quiz()
    categories = [element["category"] for element in quiz]
    return categories


def get_choosen_category(option: int) -> str:
    categories = _get_all_categories()
    for id, category in enumerate(categories):
        if (id+1) == option:
            ret_val = category

    return ret_val


def get_question(category: str) -> str:
    quiz = _get_quiz()
    questions = [element["question"] for element in quiz if element["category"] == category]
    questions_count = len(questions)
    # losuj pytanie
    import random
    random_question_num = random.randint(1, questions_count)
    return questions[random_question_num-1]




# UI

def ui_display_categories():
    categories = _get_all_categories()
    for id, category in enumerate(categories):
        print(f"{id+1} {category}")


def ui_select_option(max) -> int:
    try:
        option = int(input("Wybierz kategorię pytania "))
    except TypeError:
        raise TypeError("Wartość nie może być stringiem. Podaj liczbę od 1 do " + str(max))
    if  option < 1 or option > max:
        raise ValueError("Wartość poza zakresem. Podaj liczbę od 1 do " + str(max))

    return option


if __name__ == "__main__":
    # categories = get_all_categories()
    ui_display_categories()
    max = get_elements_count()

    option = ui_select_option(max)
    choosen_category = get_choosen_category(option)
    print()
    question = get_question(choosen_category)
    print(question)

