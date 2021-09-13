from tkinter import *
from tkinter import Canvas, messagebox

class Register():
    def __init__(self, title, controller):
        '''
        Estructura visual del Register
        Args:
            controller: Controller
            title: String
        '''
        self.controller = controller
        self.window = Tk()
        
        self.window.title(title)
        self.window.resizable(0,0)

        #Data Jugador 1
        self.labelTitle1 = Label(self.window, text="Name player 1: ",font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)
        self.entry1 = Entry(self.window, font = ("Calibri 20"))
        self.entry1.grid(row=1,column=0, columnspan = 4, pady=5,padx=5)

        #Data Jugador 2
        self.labelTitle2 = Label(self.window, text="Name player 2: ",font=("Helvetica", 10)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)
        self.entry2 = Entry(self.window, font = ("Calibri 20"))
        self.entry2.grid(row=3,column=0, columnspan = 4, pady=5,padx=5)

        #Data Jugador 3
        self.labelTitle3 = Label(self.window, text="Name player 3: ",font=("Helvetica", 10)).grid(row=4,column=0,columnspan = 4,pady=2,padx=2)
        self.entry3 = Entry(self.window, font = ("Calibri 20"))
        self.entry3.grid(row=5,column=0, columnspan = 4, pady=5,padx=5)

        #Data Jugador 4
        self.labelTitle4 = Label(self.window, text="Name player 4: ",font=("Helvetica", 10)).grid(row=6,column=0,columnspan = 4,pady=2,padx=2)
        self.entry4 = Entry(self.window, font = ("Calibri 20"))
        self.entry4.grid(row=7,column=0, columnspan = 4, pady=5,padx=5)

        self.registrar = Button(self.window, text = "Jugar", width = 8, height = 2, command = lambda: self.register()).grid(row = 8, column = 0, padx = 2, pady = 2)

    def render(self):
        '''
        Render basico del register
        '''
        self.window.mainloop()

    def get_render(self):
        '''
        Devuelve el window para renderizar en el view.py
        '''
        return self.window
          
    def register(self):
        '''
        Esta funcion extrae la informacion del register visual
        la almacena en un json/dicc y la envia al controlador
        para que el controlador la envie al modelo para que
        sea verificada
        '''
        self.json_data = {
            "jugador1":self.entry1.get(),
            "jugador2":self.entry2.get(),
            "jugador3":self.entry3.get(),
            "jugador4":self.entry4.get()
        }
        self.controller.register_players(self.json_data, self.window)