from tkinter import *
from tkinter import Canvas, messagebox


from View.tablero import Tablero

class Register():
    def __init__(self, title):
        self.aux = 0
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

        self.registrar = Button(self.window, text = "Register", width = 8, height = 2, command = self.register).grid(row = 8, column = 0, padx = 2, pady = 2)

        self.window.mainloop()
    
    def register(self):
        self.json_data = {
            "jugador1":self.entry1.get(),
            "jugador1":self.entry2.get(),
            "jugador1":self.entry3.get(),
            "jugador1":self.entry4.get()
        }
        self.window.destroy()
        tablero = Tablero('Comienza el juego', self.json_data)