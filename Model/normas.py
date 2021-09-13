from functools import *

#Falta: Verificar si cuando las fichas salen de la carcel, hay un jugador en esa posicion (en ese caso ese jugador va a su respectiva carcel)
#       Cuando haga 1 vuelta completa desviar el camino hacia el camino del triunfo
#       Implementar la clase score

class Normas():
    def __init__(self):
        '''
        Clase que incluira las normas del parques
        '''
        self.allow = None
        self.tablero = None
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def register_rule(self, data):
        '''
        Clase que incluira las normas del parques
        Args:
            data: dicc
        '''
        self.allow = True
        if ((type(data["jugador1"]) != str) or (len(data["jugador1"]) == 0) or (data["jugador1"] == data["jugador2"]) or (data["jugador1"] == data["jugador3"])):
            self.allow = False
        if ((type(data["jugador2"]) != str) or (len(data["jugador2"]) == 0) or (data["jugador2"] == data["jugador3"]) or (data["jugador2"] == data["jugador4"])):
            self.allow = False
        if ((type(data["jugador3"]) != str) or (len(data["jugador3"]) == 0) or (data["jugador3"] == data["jugador4"])):
            self.allow = False
        if ((type(data["jugador4"]) != str) or (len(data["jugador4"]) == 0) or (data["jugador4"] == data["jugador1"])):
            self.allow = False
        return self.allow

    def sacar_carcel(self, jugador):
        '''
        Verifica si el jugador(turno) cumple la condicion numeros iguales para sacar de la carcel
        Args:
            jugador: array
        '''
        self.allow = False
        if jugador[0][4]:
            if jugador[1][0] == jugador[1][1]: #jugador[1]: Contiene un array con ambos dados
                self.allow = True
        return [self.allow, jugador]
    
    def analyze_context(self, jugador, tablero, positions):
        self.tablero = tablero
        y, x = positions
        self.moves = 0
        self.moves_aux = 0
        print('Pos inicial: ' + str(y) + str(x))
        print('Jugador[0]: ' + str(jugador[0]))
        print('self.tablero[y][x]: ' + str(self.tablero[y][x]))
        for data in self.tablero:
            print(data)
        if jugador[0] == self.tablero[y][x]:
            self.number_move = reduce(lambda x, y: x+y, jugador[1])
            while (self.moves < self.number_move):
                print('Movimiento: ' + str(self.moves))
                print('Y: '+str(y))
                #Primer contexto: El jugador con el movimiento atrapa a otro jugador
                if y == 7:
                    print(' y == 7 ')
                    if x <= 7 and x > 0:
                        print(' x <= 7 and x > 0 ')
                        data = self.controller.get_value_tablero(y,x-1)
                        print('Data: ' + str(data))
                        if x == 7:
                            print(' x == 7 ')
                            if data == 'SL' or data == 'o' or data == 'S':
                                if self.moves + 1 == self.number_move:
                                    self.moves_aux = (7,7,True)
                                else:
                                    self.moves_aux = (7,7,False)
                            elif type(data) == list:
                                if self.moves + 1 == self.number_move:
                                    self.controller.meter_carcel(data)
                                    self.moves_aux = (7,7,True)
                                else:
                                    self.moves_aux = (7,7,False)
                        else:
                            if type(data) == list and (self.moves + 1 == self.number_move):
                                self.controller.meter_carcel(data)
                        x -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 0:
                        print(' x == 0 ')
                        data = self.controller.get_value_tablero(y+1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x > 9 and x <= 16:
                        print(' x > 9 and x <= 16 ')
                        data = self.controller.get_value_tablero(y,x-1)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        x -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 9:
                        print(' x == 9 ')
                        data = self.controller.get_value_tablero(y-1,x)
                        print('Data: ' + str(data))
                        if data == 'SL' or data == 'o' or data == 'S':
                            if self.moves + 1 == self.number_move:
                                self.moves_aux = (7,9,True)
                            else:
                                self.moves_aux = (7,9,False)
                        elif type(data) == list:
                            if self.moves + 1 == self.number_move:
                                self.controller.meter_carcel(data)
                                self.moves_aux = (7,9,True)
                            else:
                                self.moves_aux = (7,9,False)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y == 16:
                    print(' y == 16 ')
                    if x >= 7 and x < 9:
                        print(' x >= 7 and x < 9 ')
                        data = self.controller.get_value_tablero(y,x+1)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        x += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 9:
                        print(' x == 9 ')
                        data = self.controller.get_value_tablero(y-1, x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                                self.controller.meter_carcel(data)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y == 9:
                    print(' y == 9 ')
                    if x < 7 and x >= 0:
                        print(' x < 7 and x >= 0 ')
                        data = self.controller.get_value_tablero(y,x+1)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        x += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 7:
                        print(' x == 7 ')
                        data = self.controller.get_value_tablero(y+1,x)
                        print('Data: ' + str(data))
                        if data == 'SL' or data == 'o' or data == 'S':
                            if self.moves + 1 == self.number_move:
                                self.moves_aux = (9,7,True)
                            else:
                                self.moves_aux = (9,7,False)
                        elif type(data) == list:
                            if self.moves + 1 == self.number_move:
                                self.controller.meter_carcel(data)
                                self.moves_aux = (9,7,True)
                            else:
                                self.moves_aux = (9,7,False)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x >= 9 and x < 16:
                        print(' x >= 9 and x < 16 ')
                        data = self.controller.get_value_tablero(y,x+1)
                        print('Data: ' + str(data))
                        if x == 9:
                            if data == 'SL' or data == 'o' or data == 'S':
                                if self.moves + 1 == self.number_move:
                                    self.moves_aux = (9,9,True)
                                else:
                                    self.moves_aux = (9,9,False)
                            elif type(data) == list:
                                if self.moves + 1 == self.number_move:
                                    self.controller.meter_carcel(data)
                                    self.moves_aux = (9,9,True)
                                else:
                                    self.moves_aux = (9,9,False)
                        else:
                            if type(data) == list and (self.moves + 1 == self.number_move):
                                    self.controller.meter_carcel(data)
                        x += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 16:
                        print(' x == 0 ')
                        data = self.controller.get_value_tablero(y-1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y == 8:
                    print(' y == 8 ')
                    if x == 0:
                        print(' x == 0 ')
                        data = self.controller.get_value_tablero(y+1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 16:
                        print(' x == 0 ')
                        data = self.controller.get_value_tablero(y-1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and(self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y > 9 and y < 16:
                    print(' y > 9 and y < 16 ')
                    if x == 7:
                        print(' x == 7 ')
                        data = self.controller.get_value_tablero(y+1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 9:
                        print(' x == 7 ')
                        data = self.controller.get_value_tablero(y-1,x)
                        print('Data: ' + str(data))
                        if type(data) == list and(self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y <= 6 and y > 0:
                    print(' y <= 6 and y > 0 ')
                    if x == 9:
                        print(' x == 9 ')
                        data = self.controller.get_value_tablero(y-1, x)
                        print('Data: ' + str(data))
                        if type(data) == list and(self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 7:
                        print(' x == 9 ')
                        data = self.controller.get_value_tablero(y+1, x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                if y == 0:
                    print(' y == 0 ')
                    if x <= 9 and x > 7:
                        print(' x <= 9 and x > 7 ')
                        data = self.controller.get_value_tablero(y, x-1)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        x -= 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
                    if x == 7:
                        print(' x == 7 ')
                        data = self.controller.get_value_tablero(y+1, x)
                        print('Data: ' + str(data))
                        if type(data) == list and (self.moves + 1 == self.number_move):
                            self.controller.meter_carcel(data)
                        y += 1
                        self.moves += 1
                        print('Pos en while'+ str([y,x]))
            print('Pos antes:' + str([y, x]))
            if self.moves_aux == (7,7,False):
                if y > 7:
                    y -= 1
                else:
                    x += 1
            if self.moves_aux == (7,9,False):
                if x < 9:
                    x += 1
                else:
                    y += 1
            if self.moves_aux == (9,7,False):
                if x > 7:
                    x -= 1
                else:
                    y -= 1
            if self.moves_aux == (9,9,False):
                if y < 9:
                    y += 1
                else:
                    x -= 1
            print('Pos despues:' + str([y, x]))
            self.controller.set_value_tablero(y,x, self.tablero[y][x])
            self.controller.update_visual_coords(jugador, (x,y))
            self.controller.set_coords_player(jugador, y, x)