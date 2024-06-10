games_information = {}
games_information['Wojna o Pierścień'] = ('Galakta', 9)
games_information['Alchemicy'] = ('CGC', 7)
games_information['Cywilizacja Poprzez Wieki'] = ('Rebel', 9)

def print_game_info(game_name: str) -> tuple:
    print("Gra: " + game_name)
    print("Wydawca: " + games_information[game_name][0])
    print("Ocena: " + str(games_information[game_name][1]))


print_game_info('Wojna o Pierścień')