games = {'Fallout New Vegas', 'Civilization 5', 'Minecraft'}
games2 = {'Heroes of Might and Magic 4', 'Elder Scrolls: Skyrim', 'Civilization 5'}

# union
print(games | games2)
print(games.union(games2))

# intersection - część wspólna
print(games.intersection(games2))
print(games & games2)

# differense - różnica
print(games.difference(games2))
print(games - games2)

# simetric difference - różnica symetryczna - elementy które nie znajdują się w żadnym ze zbiorów
print(games.symmetric_difference(games2))
print(games ^ games2)