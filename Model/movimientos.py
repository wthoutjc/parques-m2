class Movimientos():
    def __init__(self):
        '''
        Estructura de los movimientos, cada jugador empienza con 0
        '''
        self.jugador = None
        self.m_jugador1 = 0
        self.m_jugador2 = 0
        self.m_jugador3 = 0
        self.m_jugador4 = 0
    
    def set_jugador(self, jugador):
        '''
        seteo del turno
        Args:
            jugador: array
        '''
        self.jugador = jugador
        self.increment_movimiento(self.jugador)

    def increment_movimiento(self, jugador):
        '''
        Dado un jugador(turno) incrementar el movimiento
        si es movimiento de sacar de carcel, cuenta como +1
        Args:
            jugador: array
        '''
        if jugador[0][3] == "0001":
            if self.m_jugador1 == 0:
                self.m_jugador1 += 1
        if jugador[0][3] == "0002":
            if self.m_jugador1 == 0:
                self.m_jugador1 += 1
        if jugador[0][3] == "0003":
            if self.m_jugador1 == 0:
                self.m_jugador1 += 1
        if jugador[0][3] == "0004":
            if self.m_jugador1 == 0:
                self.m_jugador1 += 1
    
    def get_movimiento(self, jugador):
        if jugador[0][3] == "0001":
            return self.m_jugador1
        if jugador[0][3] == "0002":
            return self.m_jugador2
        if jugador[0][3] == "0003":
            return self.m_jugador3
        if jugador[0][3] == "0004":
            return self.m_jugador4