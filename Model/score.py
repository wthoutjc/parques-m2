class Score():
    def __init__(self):
        self.jugador = None
        self.score = None

    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score