import json

def get_phones_list() -> list():
    with open('phones.json') as phones_file:
        phones = json.load(phones_file)

    return phones


def get_phone_name() -> str():
    name = input("Podaj nazwę telefonu: ")
    return name


def create_phone() -> dict():
    name = input("Podaj nazwę telefonu: ")
    color = input("Podaj kolor telefonu: ")
    memory = input("Ile telefon ma pamięci: ")
    price = input("Cena: ")

    phone = {
        'name': name
        , 'specifications': {'color': color, 'memory': memory}
        , 'price': price
    }

    return phone


def add_phone_to_list(phone_list: list, phone: dict):
    phone_list.append(phone)


def remove_phone_from_list_by_name(phone_list: list, phone_name: str):  # rzuca ValueError!!!!!!!!!!
    for index, phone in enumerate(phone_list):
        if phone['name'] == phone_name:
            del phone_list[index]

def put_list_into_file(phone_list: list):
    pass



if __name__ == "__main__":
    phones = get_phones_list()
    print(phones)
    # phone = create_phone()
    # add_phone_to_list(phones, phone)
    # print(phones)

    # removing
    phone_name = get_phone_name()
    remove_phone_from_list_by_name(phones, phone_name)
    print(phones)