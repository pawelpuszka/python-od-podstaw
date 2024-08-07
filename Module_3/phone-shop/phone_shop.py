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
        else:
            raise ValueError("Nie znaleziono telefonu")


def display_stock_list(phone_list: list):
    for phone in phone_list:
        print("Nazwa telefonu: " + phone['name'])
        print("Specyfikacja:")
        print("    Kolor : " + phone['specifications']['color'])
        print("    Pamięć: " + str(phone['specifications']['memory']))
        print("Cena: " + str(phone['price']))
        print()


def display_stock_file():
    with open('phones.json') as phones_file:
        phones = json.load(phones_file)
    for phone in phones:
        print("Nazwa telefonu: " + phone['name'])
        print("Specyfikacja:")
        print("    Kolor : " + phone['specifications']['color'])
        print("    Pamięć: " + str(phone['specifications']['memory']))
        print("Cena: " + str(phone['price']))
        print()


def _get_phone_by_name_(phone_list: list, phone_name: str) -> dict():
    tmp_phone = dict()
    for phone in phone_list:
        if phone_name == phone['name']:
            tmp_phone = phone

    return phone


def modify_phone(phone_list: list):
    print("Który telefon chcesz zmodyfikować. Podaj nazwę.")
    phone_name = get_phone_name()
    phone = _get_phone_by_name_(phone_list, phone_name)
    print("Co chcesz zmienić")
    print("1 - kolor")
    print("2 - pamięć")
    print("3 - cena")
    option = input("Podaj opcję: ")

    match option:
        case 1:
            phone['color'] = input("Podaj nowy kolor: ")
        case 2:
            phone['memory'] = input("Podaj nową wartość dla pamięci: ")
        case 3:
            phone['price'] = input("Podaj nową cenę: ")



def put_list_into_file(phone_list: list):
    pass



if __name__ == "__main__":
    phones = get_phones_list()
    print(phones)
    # phone = create_phone()
    # add_phone_to_list(phones, phone)
    # print(phones)

    # removing
    # phone_name = get_phone_name()
    # remove_phone_from_list_by_name(phones, phone_name)
    # print(phones)
    display_stock_list(phones)
    display_stock_file()
