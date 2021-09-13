import random
from random import randint
from datetime import datetime

class Partida():
    def __init__(self, jugadores):
        '''
        Clase que administra los turnos
        Args:
            jugadores: dicc
        '''
        self.jugadores = jugadores
        self.matriz = []

    def set_turno(self, jugador):
        '''
        Clase que administra los turnos
        Args:
            jugador: Array[Nombre turno score ID , fichas en carcel]
        '''
        for clave, valor in self.jugadores.items():
            if clave == jugador:
                valor[1] = True
            else:
                valor[1] = False

    def get_turno(self):
        '''
        Devuelve el turno
        '''
        if self.jugadores["jugador1"][1] == True:
            return self.jugadores["jugador1"]
        if self.jugadores["jugador2"][1] == True:
            return self.jugadores["jugador2"]
        if self.jugadores["jugador3"][1] == True:
            return self.jugadores["jugador3"]
        if self.jugadores["jugador4"][1] == True:
            return self.jugadores["jugador4"]
        return False
    
    def lanzar_dados(self):
        '''
        Crea un array de dos enteros que seran los dados
        '''
        random.seed(datetime.now())
        self.random1 = randint(1, 6)
        self.random2 = randint(1, 6)
        return [self.random1, self.random2]

    def iniciar_movimiento(self):
        '''
        Inicia el movimiento y setea los turnos
        Devuelve el turno del jugador, con su array de dados
        '''
        if self.get_turno() == False:
            self.set_turno('jugador1')
            data = [self.get_turno(), [0,0]]
            return data
        else:
            self.turno = self.get_turno()
            if self.turno[3] == "0001":
                self.set_turno('jugador2')
            if self.turno[3] == "0002":
                self.set_turno('jugador3')
            if self.turno[3] == "0003":
                self.set_turno('jugador4')
            if self.turno[3] == "0004":
                self.set_turno('jugador1')
            data = [self.turno, self.lanzar_dados()]
            return data