from Model.usuarios import Usuarios
from Model.normas import Normas
from Model.score import Score

class Model():
    def __init__(self):
        '''
        Estructura del modelo, se instancian
        las clases componente
        '''
        self.controller = None
        self.usuarios = Usuarios()
        self.normas = Normas()
        self.score = Score()
        self.jugador = None

    def set_controller(self, controller):
        '''
        importamos todas las funciones del controlador aca
        Args:
            controller: Controller
        '''
        self.controller = controller
        self.normas.set_controller(self.controller)
    
    def set_jugador(self, jugador):
        '''
        Esto para indicarle a que jugador(proceso del turno)
        aplicar las reglas de negocio
        Args:
            jugador: array
        '''
        self.jugador = jugador

    def get_jugador(self):
        '''
        Devuelve el jugador (turno)
        '''
        return self.jugador
    
    def verify_data_register(self, data):
        '''
        El modelo espera de su componente NORMAS
        una respuesta booleana del proceso de registro
        Args:
            data: dicc
        '''
        if self.normas.register_rule(data) == True:
            self.usuarios.set_players(data)
            return self.usuarios.get_players()
        else:
            self.controller.error('Datos no válidos')
            return False
    
    def es_par(self, jugador, tablero):
        '''
        El modelo espera de su componente NORMAS
        una respuesta booleana del proceso de sacar_carcel
        Args:
            jugador: array
        '''
        data = self.normas.sacar_carcel(jugador, tablero)
        if data[0]:
            self.usuarios.uptdate_info_player(jugador[0], False, 4)
            #self.usuarios.increment_movimientos(jugador)
            return data[0]

    def acept_new_movement(self, jugador, tablero, positions):
        self.normas.analyze_context(jugador, tablero, positions)
    
    def get_value_tablero(self,x,y):
        return self.controller.get_tablero_value(x,y)
    
    def meter_carcel(self, jugador):
        print('Model, meter_carcel: jugador: ' + str(jugador))
        self.usuarios.uptdate_info_player(jugador,True,4)
    
    def incrementar_score(self, score):
        self.score.set_score(score)