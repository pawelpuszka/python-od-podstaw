# Stwórz słownik który będzie przechowywał info o krajach i ich stolicach
# Dodaj do niego 5 elementów. Wyświetl dane ze słownika w formacie kraj - stolica.

countries_and_capitals = {
    'Polska': 'Warszawa'
    ,'USA': 'Waszyngton'
    ,'Słowacja': 'Bratysława'
    ,'Niemcy': 'Berlin'
    ,'Rosja': 'Moskwa'
}

for country, capital in countries_and_capitals.items():
    print(country + ' - ' + capital)