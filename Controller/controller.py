from Controller.partida import Partida
from Controller.tablero import Tablero
from functools import *

class Controller():
    def __init__(self):
        '''
        Estructura del controller
        aca se setea el modelo y la vista
        el controlador comunicara ambos
        '''
        self.view = None
        self.model = None
        self.partida = None
        self.tablero = None
        self.jugadores = None
        self.jugador = None

    def set_view(self, view):
        '''
        Importamos todas las funciones de view
        '''
        self.view = view
    
    def set_model(self, model):
        '''
        Importamos todas las funciones de model
        '''
        self.model = model
    
    def register_players(self, data, window):
        '''
        Proceso de registro completo, recibe el dicc del view
        lo manda a verificar al model y si la informacion es real
        empieza una ronda con turno para el jugador 1, seteamos el nuevo
        window y renderezimos el tablero
        Args:
            data: dicc
            window: Window TKINTER
        '''
        self.players = self.model.verify_data_register(data)
        if self.players:
            self.start_round(self.players)
            self.jugadores = self.players
            self.view.set_window(window)
            self.view.render_component('tablero', window)
        else:
            self.error('Datos no válidos')
            self.view.render_component('register', window)
    
    def start_round(self, data_players):
        '''
        Creamos una partida y le asignamos el dicc con la info
        de los jugadores, iniciamos movimientos y seteamos el jugador(turno)
        tanto para la vista como para el modelo
        Args:
            data_players: data
         '''
        self.partida = Partida(data_players)
        self.tablero = Tablero()
        self.jugador = self.partida.iniciar_movimiento()
        self.view.set_jugador(self.jugador)
        self.model.set_jugador(self.jugador)

    def movimiento(self):
        '''
        Esta interaccion no viene de View sino de tablero.py
        Le indicamos al componente partida que nos devuelva el turno y los dados
        nos da un array y ese array se lo seteamos al modelo y a la vista.
        El modelo por cada movimiento verificara diferentes normas y tomara
        acciones en base a ellas
        '''
        self.jugador = self.partida.iniciar_movimiento()
        self.view.set_jugador(self.jugador)
        self.model.set_jugador(self.jugador)
        if self.jugador[0][4] == True:
            if self.model.es_par(self.jugador):
                self.view.sacar_carcel(self.jugador)
                self.tablero.sacar_carcel(self.jugador)
        else:
            print(self.jugador)
            self.position_jugador = self.tablero.get_current_positions(self.jugador) #Diccionario con las coordenadas actuales para cada jugador
            self.instructions = self.model.acept_new_movement(self.jugador, self.tablero.get_tablero(), self.position_jugador)

    def meter_carcel(self, jugador):
        self.view.meter_carcel(jugador)
        self.model.meter_carcel(jugador)
        self.tablero.meter_carcel(jugador)

    def error(self, message):
        '''
        Le indica a la vista que renderize un mensaje de estado error
        Args:
            message: String
        '''
        self.view.render_message('error', message)

    def get_turno_str(self):
        '''
        Devuelve el turno
        '''
        return self.model.get_jugador()[0][0]
    
    def get_dados_int(self):
        '''
        Devuelve array de dados
        '''
        return reduce(lambda x, y: x+y, self.model.get_jugador()[1])

    def update_visual_coords(self, jugador, coords):
        self.view.update_tablero(jugador, coords)

    def set_coords_player(self, jugador, y, x):
        self.tablero.set_current_positions(jugador, y, x)

    def set_value_tablero(self, x, y, value):
        self.tablero.set_tablero_value(x,y,value)

    def get_value_tablero(self, x, y):
        return self.tablero.get_tablero_value(x,y)