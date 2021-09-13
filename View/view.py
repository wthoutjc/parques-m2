from tkinter import *
from tkinter import Canvas, messagebox

#Controlador
from Controller.controller import Controller

#Componentes
from View.register import Register
from View.tablero import Tablero
from View.message import Message

class View():

    def __init__(self, title, controller):
        '''
        Render basico del menu de presentacion, unica instancia de los componentes visuales
        '''
        self.jugador = None

        self.window = Tk()
        self.controller = controller
        
        self.window.title(title)
        self.window.resizable(0,0)

        self.labelTitle0 = Label(self.window, text="Parqués - UDFJC",font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)
        self.labelTitle1 = Label(self.window, text="Por: ",font=("Helvetica", 9)).grid(row=1,column=0,columnspan = 4,pady=2,padx=2)
        #self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)
        #self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)
        #self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)

        self.start = Button(self.window, text = "Start", width = 8, height = 2, command = lambda: self.render_component('register', self.window)).grid(row = 5, column = 0, padx = 2, pady = 2)

    def set_window(self, window):
        '''
        Este metodo es importante porque se usa para renderizar 
        un componente visual nuevo, entonces ese componente setea 
        su window a la clase view por medio de este metodo.
        '''
        self.window = window

    def set_jugador(self, jugador):
        self.jugador = jugador

    def render_start(self):
        '''
        Render para el menu de start
        '''
        self.window.mainloop()
    
    def render_component(self, component, window):
        '''
        Aca se renderizan los demas recursos visuales
        '''
        self.window = window
        self.window.destroy()
        if component == "register":
            self.register = Register('Register', self.controller)
        if component == "tablero":
            self.tablero = Tablero('Tablero', self.controller)

    def render_message(self, state, message):
        '''
        Crea una ventana para emitir un mensaje y un estado.
        Args:
            jugador: array
        '''
        self.message = Message('Message', state, message)

    def sacar_carcel(self, jugador):
        '''
        Esta funcion le indica al tablero actualizar una posicion
        Args:
            jugador: array
        '''
        self.tablero.sacar_carcel(jugador)
    
    def meter_carcel(self, jugador):
        '''
        Esta funcion le indica al tablero actualizar una posicion
        Args:
            jugador: array
        '''
        self.tablero.meter_carcel(jugador)

    def update_tablero(self, jugador, coords):
        self.tablero.update_tablero(jugador, coords)