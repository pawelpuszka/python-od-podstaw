import json

game = {
    'title': 'Brass Birmingham'
    ,'genre': ('strategia', 'ekonomiczna')
    ,'note': 8
    ,'played': True
    ,'similar games': [
         {'title': 'Cywilizacja poprzez wieki'}
        ,{'title': 'Clash of Cultures'}
    ]
}

json_string = json.dumps(game, indent=2)
print(json_string)

with open('test_files/game.json', 'w') as file:
    json.dump(game, file, indent=4)


