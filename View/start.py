from tkinter import *
from tkinter import Canvas, messagebox

#Componentes
from View.register import Register
class Window():
    def __init__(self, title):
        self.aux = 0
        self.window = Tk()
        
        self.window.title(title)
        self.window.resizable(0,0)

        self.labelTitle0 = Label(self.window, text="Parqués - UDFJC",font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)
        self.labelTitle1 = Label(self.window, text="Por: ",font=("Helvetica", 9)).grid(row=1,column=0,columnspan = 4,pady=2,padx=2)
        self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)
        self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)
        self.name0 = Label(self.window, text="Juan Camilo Ramírez Rátiva - 20181020089",font=("Helvetica", 8)).grid(row=2,column=0,columnspan = 4,pady=2,padx=2)

        self.btn_ac = Button(self.window, text = "Start", width = 8, height = 2, command = self.render_tablero).grid(row = 5, column = 0, padx = 2, pady = 2)

        self.window.mainloop()

    def render_tablero(self):
        self.window.destroy()
        self.tablero = Register('Register Section')