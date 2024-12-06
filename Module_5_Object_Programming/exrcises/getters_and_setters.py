class BoardGame:
    def __init__(self, name2, genre, rating):
        self._name = name2
        self.genre = genre
        self.rating = rating
        
    @property
    def _name(self):
        return self.name2
    
    @_name.setter
    def _name(self, name):
        self.name = name2.upper()
        
        
        
civilisation = BoardGame('Civilisation Through The Ages', 'Strategy', 8.5)
print(civilisation.name)