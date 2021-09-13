class Tablero():
    def __init__(self):
        self.controller = None
        self.tablero = [
            ['C','x','x','x','x','x','x','o','S','o','x','x','x','x','x','x','C'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','SL','o','S','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['o','o','o','o','S','o','o','o','o','o','o','o','SL','o','o','o','o'],
            ['S','o','o','o','o','o','o','o','L','o','o','o','o','o','o','o','S'],
            ['o','o','o','o','SL','o','o','o','o','o','o','o','S','o','o','o','o'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','S','o','SL','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['x','x','x','x','x','x','x','o','o','o','x','x','x','x','x','x','x'],
            ['C','x','x','x','x','x','x','o','S','o','x','x','x','x','x','x','C'],
        ]
        self.coord_j1 = None
        self.coord_j2 = None
        self.coord_j3 = None
        self.coord_j4 = None

    def set_controller(self, controller):
        self.controller = controller

    def set_tablero_value(self, y, x, valor):
        self.tablero[y][x] = valor

    def get_tablero_value(self, y, x):
        return self.tablero[y][x]

    def get_tablero(self):
        return self.tablero
    
    def set_current_positions(self, jugador, y, x):
        if jugador[0][3] == "0001": #azul
            self.coord_j1 = [y,x]
        if jugador[0][3] == "0002": #amarillo
            self.coord_j2 = [y,x]
        if jugador[0][3] == "0003": #verde
            self.coord_j3 = [y,x]
        if jugador[0][3] == "0004": #roja
            self.coord_j4 = [y,x]

    def get_current_positions(self, jugador):
        if jugador[0][3] == "0001": #azul
            return self.coord_j1
        if jugador[0][3] == "0002": #amarillo
            return self.coord_j2
        if jugador[0][3] == "0003": #verde
            return self.coord_j3
        if jugador[0][3] == "0004": #roja
            return self.coord_j4

    def sacar_carcel(self, jugador):
        if jugador[0][3] == "0001": #azul
            self.set_tablero_value(4,7, jugador[0])
            self.coord_j1 = [4,7]
        if jugador[0][3] == "0002": #amarillo
            self.set_tablero_value(9,4, jugador[0])
            self.coord_j2 = [9,4]
        if jugador[0][3] == "0003": #verde
            self.set_tablero_value(7,12, jugador[0])
            self.coord_j3 = [7,12]
        if jugador[0][3] == "0004": #roja
            self.set_tablero_value(12,9, jugador[0])
            self.coord_j4 = [12,9]
    
    def meter_carcel(self, jugador):
        if jugador[3] == "0001": #azul
            self.set_tablero_value(0,0, jugador[0])
            self.coord_j1 = [0,0]
        if jugador[3] == "0002": #amarillo
            self.set_tablero_value(16,0, jugador[0])
            self.coord_j2 = [16,0]
        if jugador[3] == "0003": #verde
            self.set_tablero_value(0,16, jugador[0])
            self.coord_j3 = [0,16]
        if jugador[3] == "0004": #roja
            self.set_tablero_value(16,16, jugador[0])
            self.coord_j4 = [16,16]