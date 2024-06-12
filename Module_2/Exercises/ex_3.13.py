# 13. Napisz funkcję, która przyjmuje dwa słowniki i zwraca listę kluczy z obu słowników.

def get_keys(dict1: dict, dict2: dict) -> list():
    countries = list()

    for country in dict1.keys():
        countries.append(country)

    for country in dict2.keys():
        countries.append(country)

    return countries


nato = {
    'USA': 'Waszyngton'
    ,'Francja': 'Paryż'
    ,'Niemcy': 'Berlin'
    ,'Austria': 'Wiedeń'
}

warsaw_pact = {
    'Polska': 'Warszawa'
    ,'Rosja': 'Moskwa'
    ,'Czechy': 'Praga'
    ,'Białoruś': 'Mińsk'
}

print(get_keys(nato, warsaw_pact))