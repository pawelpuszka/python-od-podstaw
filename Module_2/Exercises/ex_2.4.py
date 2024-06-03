# Stwórz listę którą wypełnisz imionami - po 5 imion w każdej z list.
# Zadbaj o to aby niektóre imiona się powtarzały tzn były obecna na obu listach
# Wyświetl powtarzające się imiona.

# ver.1
names_1 = ['Paweł', 'Ania', 'Filip', 'Antek']
names_2 = ['Marek', 'Grażyna', 'Maciek', 'Ania']

names_1 = set(names_1)
names_2 = set(names_2)

print(names_1.intersection(names_2))


# ver.2
names_1 = ['Paweł', 'Ania', 'Filip', 'Antek']
names_2 = ['Marek', 'Grażyna', 'Maciek', 'Ania']

for name1 in names_1:
    for name2 in names_2:
        if name1 == name2:
            print(name1)