from tkinter import *
from tkinter import Canvas, messagebox

class Message():
    def __init__(self, title, state, message):
        '''
        Render basico del menu de presentacion, unica instancia de los componentes visuales
        '''
        self.state = state
        self.message = message
        self.window = Tk()
        
        self.window.title(title)
        self.window.resizable(0,0)

        if state == 'error':
            self.labelTitle0 = Label(self.window, text=str('Error' + message),font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)
        self.labelTitle0 = Label(self.window, text=str('Success' + message),font=("Helvetica", 10)).grid(row=0,column=0,columnspan = 4,pady=2,padx=2)
        self.close = Button(self.window, text = "OK", width = 8, height = 2, command = self.window.destroy).grid(row = 1, column = 0, padx = 2, pady = 2)

        self.window.mainloop()