# 5. Korzystając z list z poprzedniego ćwiczenia wyświetl
# tylko te imiona które są obecne w pierwszej liście

# ver.1
names_1 = ['Paweł', 'Ania', 'Filip', 'Antek']
names_2 = ['Marek', 'Grażyna', 'Maciek', 'Ania']

names_1 = set(names_1)
names_2 = set(names_2)

print(names_1.difference(names_2))


# ver.2
names_1 = ['Paweł', 'Ania', 'Filip', 'Antek']
names_2 = ['Marek', 'Grażyna', 'Maciek', 'Ania']

for name1 in names_1:
    for name2 in names_2:
        if name1 == name2:
            names_1.remove(name1)

print(names_1)