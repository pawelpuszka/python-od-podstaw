# Posortuj słownik z poprzedniego ćwiczenia w kolejności alfabetycznej

# ver.1
countries_and_capitals = {
    'Polska': 'Warszawa'
    ,'USA': 'Waszyngton'
    ,'Słowacja': 'Bratysława'
    ,'Niemcy': 'Berlin'
    ,'Austria': 'Wiedeń'
}

countries = list(countries_and_capitals.keys())
countries.sort()
countries_and_capitals_sorted = {country: countries_and_capitals[country] for country in countries}
print(countries_and_capitals_sorted)

# ver.2
countries_and_capitals = {
    'Polska': 'Warszawa'
    ,'USA': 'Waszyngton'
    ,'Słowacja': 'Bratysława'
    ,'Niemcy': 'Berlin'
    ,'Austria': 'Wiedeń'
}

countries_and_capitals_sorted = dict(sorted(countries_and_capitals.items()))
print(countries_and_capitals_sorted)