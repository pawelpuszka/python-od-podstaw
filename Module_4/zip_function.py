names = ['Paweł', 'Ania', 'Filip', 'Antek']
games = ['Wojan o Pierścień', 'Cywilizacja poprzez wieki', 'Fallout Wasteland Warfare', 'Podróże przez Śródżiemie']

for name, game in zip(names, games):
    print(f"{name} - {game}")


fav_games = list(zip(names, games))
print(fav_games)


# łączenie list o różnej długości
from itertools import zip_longest, cycle

names = ['Paweł', 'Ania', 'Filip', 'Antek']
games = ['Wojan o Pierścień', 'Cywilizacja poprzez wieki', 'Fallout Wasteland Warfare']

fav_games = list(zip_longest(names, games))
print(fav_games)

fav_games = list(zip(names, cycle(games)))
print(fav_games)