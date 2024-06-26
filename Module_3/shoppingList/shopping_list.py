import os
LISTS_DIR = 'shopping_lists/'
LIST_FILE_EXT = '.txt'
LIST_DIRECTORY = str()
distinct_products = set()

# LIST_DIRECTORY = str()

def create_list_dir(list_name: str):
    global LIST_DIRECTORY
    LIST_DIRECTORY = LISTS_DIR + list_name + LIST_FILE_EXT


def get_list_directory():
    global LIST_DIRECTORY
    return LIST_DIRECTORY


def create_list(list_name: str):  # może rzucić wyjątek FileExists , FileNotFoundError
    tmp_name = list_name.strip()
    tmp_name = tmp_name.replace(' ', '_')
    create_list_dir(tmp_name)
    print(LIST_DIRECTORY)

    if os.path.exists(get_list_directory()):
        raise FileExistsError("shopping_list_logic.create_list(): Plik już istnieje")

    with open(get_list_directory(), 'x') as file:
        file.write(list_name.strip() + '\n')


def get_list_name():
    return input("Podaj nazwę listy: ")


# def remove_list(list_name: str):  # FileNotFoundError
#     if not os.path.exists(get_list_directory()):
#         raise FileNotFoundError("shopping_list_logic.remove_list(): Taki plik nie istnieje")
#
#     os.remove(list_dir)


def get_product_from_user():
    return input("Podaj produkt: ")


def add_product_to_shop_list(product: str):
    global distinct_products
    if product not in distinct_products:
        with open(get_list_directory(), 'a') as file:
            file.write(product + '\n')
            distinct_products.add(product)


def print_shopping_list():
    with open(get_list_directory(), 'r') as file:
        file.seek(0)
        file_content = file.read()

    print(file_content)


def remove_product_from_shop_list(item: str):
    products: list()
    with open(get_list_directory(), 'r') as file:
        products = file.readlines()
    with open(get_list_directory(), 'w') as output:
        for product in products:
            if product.strip('\n') != item:
                output.write(product)



if __name__ == "__main__":
    list_name = get_list_name()
    create_list(list_name)

    print("Dodawanie produktów do listy")
    product = get_product_from_user()
    add_product_to_shop_list(product)
    product = get_product_from_user()
    add_product_to_shop_list(product)
    product = get_product_from_user()
    add_product_to_shop_list(product)
    print_shopping_list()

    print("Usuwanie produktu z listy")
    product = get_product_from_user()
    remove_product_from_shop_list(product)
    print_shopping_list()

    print("Usunięcie listy")
    remove_list()
