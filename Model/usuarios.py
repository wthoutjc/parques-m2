from Model.movimientos import Movimientos
from Model.score import Score

class Usuarios():
    def __init__(self):
        '''
        Estructura del manejo de la información de los usuarios
        '''
        self.jugador1 = [None,False,0,'0001',True] #Nombre, turno e ID, score, jugadores en la carcel
        self.jugador2 = [None,False,0,'0002',True]
        self.jugador3 = [None,False,0,'0003',True]
        self.jugador4 = [None,False,0,'0004',True]

        self.score = None

        self.players = {
            "jugador1":self.jugador1,
            "jugador2":self.jugador2,
            "jugador3":self.jugador3,
            "jugador4":self.jugador4
        }
        
        self.movimientos = Movimientos()
    
    def set_players(self, data):
        '''
        Setea la informacion de los jugadores
        Args:
            data: dicc
        '''
        self.jugador1[0] = data["jugador1"]
        self.jugador2[0] = data["jugador2"]
        self.jugador3[0] = data["jugador3"]
        self.jugador4[0] = data["jugador4"]

    def uptdate_info_player(self, jugador, value, position):
        '''
        Actualiza la informacion de los jugadores
        Args:
            jugador: Array[Nombre, turno, ID, score, fichas en la carcel]
            value: valor de una posicion, puede ser str, int o bool
            position: int

        '''
        jugador[position] = value

    def increment_movimientos(self, jugador):
        '''
        Administra por medio de movimientos.py el numero de movimientos
        esta class nos sirve luego para hacer validaciones de normas
        Args:
            jugador: Array[Nombre, turno, ID, score, fichas en la carcel]
        '''
        self.movimientos.set_jugador(jugador)

    def get_players(self):
        '''
        Devuelve el dicc con la info de los jugadores
        '''
        return self.players