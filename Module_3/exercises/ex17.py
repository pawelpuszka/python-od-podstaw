# Stwórz aplikację, która pozwala użytkownikom tworzyć, usuwać i aktualizować zadania. Zadania powinny być przechowywane w pliku JSON.
# Każde zadanie powinno mieć tytuł, opis i status (np. “do zrobienia”, “w trakcie”, “zrobione”).

import json

def get_task() -> tuple:
    task_name = input("Nazwa zadania ")
    task_desc = input("Opis zadania ")
    return task_name, task_desc

def _get_max_task_number() -> int():
    with open('../test_files/tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        order_nums = [task["id"] for task in tasks]
        return max(order_nums)


def task_to_dict(task: tuple()) -> dict:
    task_name, task_desc = task
    next_num = _get_max_task_number() + 1
    task = {
        "id": next_num,
        "nazwa": task_name,
        "opis": task_desc,
        "status": "do zrobienia"
    }
    return task


def _read_tasks_list() -> list:
    with open('../test_files/tasks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def add_one_task_to_file(task: dict):
    tasks_list = _read_tasks_list()
    tasks_list.append(task)
    with open('../test_files/tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks_list, file, indent=4, ensure_ascii=False)


def _get_task_number_from_user(oper: str) -> int:
    max_id = _get_max_task_number()
    ids = {x for x in range(1, max_id+1)}
    task_num = int(input(f"Podaj numer zadania które chcesz {oper} "))
    if task_num in ids:
        return task_num
    raise ValueError("Taki numer zadania nie istnieje")


def _add_tasks_to_file(tasks_list: list):
    with open('../test_files/tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks_list, file, indent=4, ensure_ascii=False)


def _reorganise_ids(tasks_list):
    max = len(tasks_list)
    for i in range(0, max):
        if tasks_list[i]["id"] != i + 1:
            tasks_list[i]["id"] = i + 1


def remove_task():
    task_num = _get_task_number_from_user("usunąć")
    tasks = _read_tasks_list()
    for task in tasks:
        if task["id"] == task_num:
            tasks.remove(task)
    _reorganise_ids(tasks)
    _add_tasks_to_file(tasks)


def change_task_name():
    try:
        task_num = _get_task_number_from_user("edytować")
    except ValueError():
        print("Taki numer zadania nie istnieje")
    tasks_list = _read_tasks_list()
    for task in tasks_list:
        if task["id"] == task_num:
            task["nazwa"] = input("Podaj nową nazwę dla zadania ")
    _add_tasks_to_file(tasks_list)


def change_task_desc():
    try:
        task_num = _get_task_number_from_user("edytować")
    except ValueError():
        print("Taki numer zadania nie istnieje")

    tasks_list = _read_tasks_list()
    for task in tasks_list:
        if task["id"] == task_num:
            task["opis"] = input("Podaj nowy opis dla zadania ")
    _add_tasks_to_file(tasks_list)


def _get_statuses_list_() -> list:
    return ["do zrobienia", "w trakcie", "zrobione"]


def _print_statuses():
    statuses = _get_statuses_list_()
    i = 1
    for status in statuses:
        print(f"{i} {status}")
        i += 1


def _get_status_id():
    status_id = int(input("Podaj numer statusu "))
    if status_id < 0 or status_id > 3:
        raise ValueError("Nie ma takiego numeru statusu")

    return status_id


def change_task_status():
    try:
        task_num = _get_task_number_from_user("edytować")
    except ValueError():
        print("Taki numer zadania nie istnieje")

    _print_statuses()
    status_id = _get_status_id()
    statuses_list = _get_statuses_list_()
    tasks_list = _read_tasks_list()

    for task in tasks_list:
        if task["id"] == task_num:
            task["status"] = statuses_list[status_id-1]

    _add_tasks_to_file(tasks_list)


def display_all_tasks():
    with open('../test_files/tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        for task in tasks:
            print(f'{task["id"]} {task["nazwa"]}')


if __name__ == "__main__":
    # task = get_task()
    # task = task_to_dict(task)
    # add_one_task_to_file(task)

    display_all_tasks()
    # change_task_name()
    # change_task_desc()
    change_task_status()

    display_all_tasks()


    # print(read_tasks_list())



