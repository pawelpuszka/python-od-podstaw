import json


text = """[
    {
         "title": "Podróże przez Śródziemie"
        ,"genre": ["fantasy", "adventure", "LOTR"]
        ,"played": true 
        ,"rank": 8   
    },
    {
         "title": "Terraformacja Marsa"
        ,"genre": ["sci-fi", "deck-building"]
        ,"played": true 
        ,"rank": 7   
    }
]"""

games = json.loads(text)
print(games[0]['genre'][1])