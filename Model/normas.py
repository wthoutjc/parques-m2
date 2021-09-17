from functools import *

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
        '''[0]
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

    def sacar_carcel(self, jugador, tablero):
        '''
        Verifica si el jugador(turno) cumple la condicion numeros iguales para sacar de la carcel
        Args:
            jugador: array
        '''
        print(jugador)
        self.allow = False
        if jugador[0][4]:
            if jugador[1][0] == jugador[1][1]: #jugador[1]: Contiene un array con ambos dados
                if jugador[0][3] == "0001":
                    data = self.controller.get_value_tablero(4, 7)
                    if type(data) == list:
                        self.controller.meter_carcel(data)
                if jugador[0][3] == "0002":
                    data = self.controller.get_value_tablero(9, 4)
                    if type(data) == list:
                        self.controller.meter_carcel(data)
                if jugador[0][3] == "0003":
                    data = self.controller.get_value_tablero(7, 12)
                    if type(data) == list:
                        self.controller.meter_carcel(data)
                if jugador[0][3] == "0004":
                    data = self.controller.get_value_tablero(12, 9)
                    if type(data) == list:
                        self.controller.meter_carcel(data)
                self.allow = True
        return [self.allow, jugador]
    
    def analyze_context(self, jugador, tablero, positions):
        self.tablero = tablero
        y, x = positions

        # Comprobamos si ya da una vuelta PARTE 1
        
        self.dio_vuelta_j1 = False
        self.dio_vuelta_j2 = False
        self.dio_vuelta_j3 = False
        self.dio_vuelta_j4 = False
        if jugador[0][3] == "0001":
            if x == 8 and y >= 0 and y < 8:
                self.dio_vuelta_j1 = True
        if jugador[0][3] == "0002":
            if y == 8 and x >= 0 and x < 8: 
                self.dio_vuelta_j2 = True
        if jugador[0][3] == "0003":
            if y == 8 and x <= 16 and x > 8:
                self.dio_vuelta_j3 = True
        if jugador[0][3] == "0004":
            if x == 8 and y <= 16 and y > 8:
                self.dio_vuelta_j4 = True
        
        self.moves = 0
        self.moves_aux = 0
        self.moves_per_if = 0
        self.pos_inicial = [y,x]
        print('Pos inicial: ' + str(y) + str(x))
        print('Jugador[0]: ' + str(jugador[0]))
        print('self.tablero[y][x]: ' + str(self.tablero[y][x]))
        if jugador[0] == self.tablero[y][x]:
            self.number_move = reduce(lambda x, y: x+y, jugador[1])
            while (self.moves < self.number_move):
                print('Movimiento: ' + str(self.moves))
                print('Y: '+str(y))
                self.moves_per_if = 0
                #Primer contexto: El jugador con el movimiento atrapa a otro jugador
                if y == 7:
                    print(' y == 7 ')
                    if x <= 7 and x > 0:
                        if self.moves_per_if == 0:
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
                                        self.moves_aux = (7,7,True)
                                    else:
                                        self.moves_aux = (7,7,False)
                            x -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 0:
                        if self.moves_per_if == 0:
                            print(' x == 0 ')
                            data = self.controller.get_value_tablero(y+1,x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x > 9 and x <= 16:
                        if self.moves_per_if == 0:
                            print(' x > 9 and x <= 16 ')
                            data = self.controller.get_value_tablero(y,x-1)
                            print('Data: ' + str(data))
                            x -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 9:
                        if self.moves_per_if == 0:
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
                                    self.moves_aux = (7,9,True)
                                else:
                                    self.moves_aux = (7,9,False)
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 8:
                        if self.moves_per_if == 0:
                            print(' x > 9 and x <= 16 ')
                            data = self.controller.get_value_tablero(y+1,x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                if y == 16:
                    print(' y == 16 ')
                    if x >= 7 and x < 9:
                        if self.moves_per_if == 0:
                            print(' x >= 7 and x < 9 ')
                            data = self.controller.get_value_tablero(y,x+1)
                            print('Data: ' + str(data))
                            x += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                            if x == 8:
                                if jugador[0][3] == '0004':
                                    print(' Jugador 4 completa vuelta ')
                                    self.dio_vuelta_j4 = True
                    if x == 9:
                        if self.moves_per_if == 0:
                            print(' x == 9 ')
                            data = self.controller.get_value_tablero(y-1, x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                if y == 9:
                    print(' y == 9 ')
                    if x < 7 and x >= 0:
                        if self.moves_per_if == 0:
                            print(' x < 7 and x >= 0 ')
                            data = self.controller.get_value_tablero(y,x+1)
                            print('Data: ' + str(data))
                            x += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 7:
                        if self.moves_per_if == 0:
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
                                    self.moves_aux = (9,7,True)
                                else:
                                    self.moves_aux = (9,7,False)
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x >= 9 and x < 16:
                        if self.moves_per_if == 0:
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
                                        self.moves_aux = (9,9,True)
                                    else:
                                        self.moves_aux = (9,9,False)
                            x += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 16:
                        if self.moves_per_if == 0:
                            print(' x == 0 ')
                            data = self.controller.get_value_tablero(y-1,x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 8:
                        if self.moves_per_if == 0:
                            print(' x == 0 ')
                            data = self.controller.get_value_tablero(y-1,x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                if y == 8:
                    print([y,x])
                    print(' y == 8 ')
                    if x == 0:
                        if self.moves_per_if == 0:
                            print(' x == 0 ')
                            data = self.controller.get_value_tablero(y+1,x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                            if jugador[0][3] == '0002':
                                print(' Jugador 2 completa vuelta ')
                                self.dio_vuelta_j2 = True
                    if x == 16:
                        if self.moves_per_if == 0:
                            print(' x == 0 ')
                            data = self.controller.get_value_tablero(y-1,x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                            if jugador[0][3] == '0003':
                                print(' Jugador 3 completa vuelta ')
                                self.dio_vuelta_j3 = True
                    if x > 0 and x < 8:
                        if self.moves_per_if == 0:
                            print(' x > 0 and x < 8 ')
                            data = self.controller.get_value_tablero(y,x+1)
                            print('Data: ' + str(data))
                            x += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x > 8 and x < 16:
                        if self.moves_per_if == 0:
                            print(' x > 0 and x < 8 ')
                            data = self.controller.get_value_tablero(y,x-1)
                            print('Data: ' + str(data))
                            x -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 8:
                        if jugador[0][3] == '0001':
                            if self.moves_per_if == 0:
                                print(' x == 8 ')
                                data = self.controller.get_value_tablero(y+1,x)
                                print('Data: ' + str(data))
                                y += 1
                                self.moves += 1
                                self.moves_per_if += 1
                                print('Pos en while'+ str([y,x]))
                        if jugador[0][3] == '0002':
                            if self.moves_per_if == 0:
                                print(' x == 8 ')
                                data = self.controller.get_value_tablero(y,x+1)
                                print('Data: ' + str(data))
                                x += 1
                                self.moves += 1
                                self.moves_per_if += 1
                                print('Pos en while'+ str([y,x]))
                        if jugador[0][3] == '0003':
                            if self.moves_per_if == 0:
                                print(' x == 8 ')
                                data = self.controller.get_value_tablero(y,x-1)
                                print('Data: ' + str(data))
                                x -= 1
                                self.moves += 1
                                self.moves_per_if += 1
                                print('Pos en while'+ str([y,x]))
                        if jugador[0][3] == '0004':
                            if self.moves_per_if == 0:
                                print(' x == 8 ')
                                data = self.controller.get_value_tablero(y-1,x)
                                print('Data: ' + str(data))
                                y -= 1
                                self.moves += 1
                                self.moves_per_if += 1
                                print('Pos en while'+ str([y,x]))
                if y > 9 and y < 16:
                    print(' y > 9 and y < 16 ')
                    if x == 7:
                        if self.moves_per_if == 0:
                            print(' x == 7 ')
                            data = self.controller.get_value_tablero(y+1,x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 9:
                        if self.moves_per_if == 0:
                            print(' x == 7 ')
                            data = self.controller.get_value_tablero(y-1,x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 8:
                        if self.moves_per_if == 0:
                            print(' x == 8 ')
                            data = self.controller.get_value_tablero(y-1,x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                if y <= 6 and y > 0:
                    print(' y <= 6 and y > 0 ')
                    if x == 9:
                        if self.moves_per_if == 0:
                            print(' x == 9 ')
                            data = self.controller.get_value_tablero(y-1, x)
                            print('Data: ' + str(data))
                            y -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 7:
                        if self.moves_per_if == 0:
                            print(' x == 9 ')
                            data = self.controller.get_value_tablero(y+1, x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                    if x == 8:
                        if self.moves_per_if == 0:
                            print(' x == 8 ')
                            data = self.controller.get_value_tablero(y+1, x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
                if y == 0:
                    print(' y == 0 ')
                    if x <= 9 and x > 7:
                        if self.moves_per_if == 0:
                            print(' x <= 9 and x > 7 ')
                            data = self.controller.get_value_tablero(y, x-1)
                            print('Data: ' + str(data))
                            x -= 1
                            self.moves += 1
                            self.moves_per_if += 1
                            if x == 8:
                                if jugador[0][3] == '0001':
                                    print(' Jugador 1 completa vuelta ')
                                    self.dio_vuelta_j1 = True
                        print('Pos en while'+ str([y,x]))
                    if x == 7:
                        if self.moves_per_if == 0:
                            print(' x == 7 ')
                            data = self.controller.get_value_tablero(y+1, x)
                            print('Data: ' + str(data))
                            y += 1
                            self.moves += 1
                            self.moves_per_if += 1
                            print('Pos en while'+ str([y,x]))
            print('Pos antes:' + str([y, x]))
            print('moves_aux: ' + str(self.moves_aux))
            if self.moves_aux == (7,7,False):
                if y == 7:
                    x += 1
                if y > 7 and y < 9:
                    y -= 1
                if y == 9:
                    if x == 0:
                        y -= 1
                    if x > 0:
                        x -= 1
            if self.moves_aux == (7,7,True):
                x = 7
                y = 7
            if self.moves_aux == (7,9,False):
                if y < 7 and y > 0:
                    if x == 9:
                        y += 1
                    if x < 9 and x > 7:
                        x += 1
                    if x == 7:
                        y -= 1
                if y == 0:
                    if x == 7:
                        x += 1 
            if self.moves_aux == (7,9,True):
                y = 7
                x = 9
            if self.moves_aux == (9,7,False):
                if y > 9 and y < 16:
                    if x == 7:
                        y -= 1
                    if x == 9:
                        y += 1
                if y == 16:
                    if x == 7:
                        y -= 1
                    if x > 7 and x <= 9:
                        x -= 1
            if self.moves_aux == (9,7,True):
                y = 9
                x = 7
            if self.moves_aux == (9,9,False):
                if y == 9:
                    if x > 9 and x <= 16:
                        x -= 1
                if y == 7:
                    if x == 16:
                        y += 1
                    if x < 16:
                        x += 1
            if self.moves_aux == (9,9,True):
                y = 9
                x = 9
            print('Pos despues PARTE1:' + str([y, x]))

            # Comprobamos si ya da una vuelta PARTE 2
            # Si llega la coordenada (8,8) incrementa el score en 1 y pone otros jugadores en la carcel
            # Dependiendo de cada jugador rebotar el limite, ej: si el jugador 4 tira dados y sobre pasa (8,8) restar ese excedente y bajarlo a la posicion de la linea ganadora
            if jugador[0][3] == "0001":
                print('Jugador 1' + str(self.dio_vuelta_j1))
            if jugador[0][3] == "0002":
                print('Jugador 2' + str(self.dio_vuelta_j2))
            if jugador[0][3] == "0003":
                print('Jugador 3' + str(self.dio_vuelta_j3))
            if jugador[0][3] == "0004":
                print('Jugador 4' + str(self.dio_vuelta_j4))

            if jugador[0][3] == "0001" and self.dio_vuelta_j1 == True:
                self.pos_j1 = (0, 8)
                self.excedente = abs(self.pos_j1[0] - y) + abs(self.pos_j1[1] - x)
                #print('EXCENDETE: ' + str(self.excedente))
                x = 8
                y = self.excedente
                if y > 8:
                    x = 8
                    y = 8
            if jugador[0][3] == "0002" and self.dio_vuelta_j2 == True:
                self.pos_j4 = (8, 0)
                self.excedente = abs(self.pos_j4[0] - y) + abs(self.pos_j4[1] - x)
                y = 8
                x = self.excedente
                if x > 8:
                    x = 8
                    y = 8
            if jugador[0][3] == "0003" and self.dio_vuelta_j3 == True:
                self.pos_j4 = (8, 16)
                self.excedente = abs(self.pos_j4[0] - y) + abs(self.pos_j4[1] - x)
                x = self.excedente
                y = 8
                if x < 8:
                    x = 8
                    y = 8
            if jugador[0][3] == "0004" and self.dio_vuelta_j4 == True:
                self.pos_j4 = (16, 8)
                self.excedente = abs(self.pos_j4[0] - y) + abs(self.pos_j4[1] - x)
                x = 8
                y = self.excedente
                if y < 8:
                    x = 8
                    y = 8
            
            print('Pos despues PARTE2:' + str([y, x]))
            # Conseguir el valor original de la matriz estado 0:
            self.valor_original = self.controller.get_valor_original(self.pos_inicial[0], self.pos_inicial[1])

            # Setear ese valor original a las posiciones iniciales para limpiar la matriz padre
            self.controller.set_value_tablero(self.pos_inicial[0], self.pos_inicial[1], self.valor_original)

            # Comprobamos si el valor par actualizar la matriz contiene otro jugador, en ese caso a la carcel
            data = self.controller.get_value_tablero(y, x)
            if type(data) == list:
                if self.controller.get_valor_original(y, x) != 'S':
                    self.controller.meter_carcel(data)

            # Si coordenadas 8,8 aumenta el score y a la carcel
            if x == 8 and y == 8:
                self.controller.meter_carcel(jugador[0])
                self.controller.aumentar_score(jugador)
            else:
                # Setea el jugador en la nueva posicion calculada
                self.controller.set_value_tablero(y,x, jugador[0])

                # Actualiza las coordenadas visuales
                self.controller.update_visual_coords(jugador, (x,y))

                # Actualiza las coordendas logicas
                self.controller.set_coords_player(jugador, y, x)