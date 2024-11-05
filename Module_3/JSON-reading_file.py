# import json
#
# with open('test_files/game.json') as json_file:
#     games = json.load(json_file)
#     print(games)
#     print(games[1]['title'])


from datetime import datetime

now = datetime.now()

print(now.strftime("%H:%M:%S"))
