class Score():
    def __init__(self):
        self.score_j1 = 0
        self.score_j2 = 0
        self.score_j3 = 0
        self.score_j4 = 0

    def aumentar_score(self, jugador):
        if jugador[0][3] == '0001':
            self.score_j1 += 1
        if jugador[0][3] == '0002':
            self.score_j2 += 1
        if jugador[0][3] == '0003':
            self.score_j3 += 1
        if jugador[0][3] == '0004':
            self.score_j4 += 1
    
    def get_score(self, jugador):
        if jugador[0][3] == '0001':
            return self.score_j1
        if jugador[0][3] == '0002':
            return self.score_j2
        if jugador[0][3] == '0003':
            return self.score_j3
        if jugador[0][3] == '0004':
            return self.score_j4 