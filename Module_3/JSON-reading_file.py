import json

with open('test_files/game.json') as json_file:
    games = json.load(json_file)
    print(games)
    print(games[1]['title'])
