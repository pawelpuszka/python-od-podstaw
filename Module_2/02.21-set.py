games = {}  # pusty set

games = {'Fallout New Vegas', 'Civilization 5', 'Minecraft'}
print(games)

#  w secie nie ma kolejności obiektóœ, brak indeksów
# set nie pozwoli na istnienie takich samych obiektów - duplikaty usunie

games.add('Baldur\'s Gate')
print(games)

games.remove('Fallout New Vegas')
print(games)

games.update(('Heroes of Might and Magic 4', 'Elder Scrolls: Skyrim'))  # może być set, lista lub tupla

for game in games:
    print(game)

