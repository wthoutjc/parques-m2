from tkinter import *
from tkinter import Frame, Canvas
from PIL import Image, ImageTk

class Tablero():
    def __init__(self, title, controller):
        '''
        Estructura visual del tablero
        Args:
            controller: Controller
            title: String
        '''
        self.controller = controller
        self.window = Tk()
        
        self.frame = Frame(self.window)
        self.frame.pack()

        self.window.title(title)
        self.window.geometry("800x930")
        self.window.resizable(width=0, height=0)

        self.canvas = Canvas(self.frame, bg="black", width=1200, height=800)
        self.canvas.pack()

        self.background = Image.open("View/images/background.png")
        self.background.thumbnail((1200,800)) # Redimension (Alto, Ancho)
        self.background = ImageTk.PhotoImage(self.background)
        self.canvas.create_image((400,401), image=self.background)

        self.string_turno = StringVar()
        self.string_turno.set("Turno: " + str(self.controller.get_turno_str()))
        self.label_turno = Label(self.window, text=self.string_turno.get(),font=("Monserrat", 16))
        self.label_turno.place(x=10,y=810)

        self.string_dados = StringVar()
        self.string_dados.set("Dados: " + str(self.controller.get_dados_int()))
        self.label_dados = Label(self.window, text=self.string_dados.get(),font=("Monserrat", 16))
        self.label_dados.place(x=10,y=850)

        self.string_dados = StringVar()
        self.string_dados.set("Dados: " + str(self.controller.get_dados_int()))
        self.label_dados = Label(self.window, text=self.string_dados.get(),font=("Monserrat", 16))
        self.label_dados.place(x=10,y=850)

        self.img_fazul = Image.open("View/images/jugadores/azul.png").resize((30,50), Image.ANTIALIAS)
        self.img_fazul = ImageTk.PhotoImage(self.img_fazul)

        self.img_famarillo = Image.open("View/images/jugadores/amarillo.png").resize((30,50), Image.ANTIALIAS)
        self.img_famarillo = ImageTk.PhotoImage(self.img_famarillo)

        self.img_fverde = Image.open("View/images/jugadores/verde.png").resize((30,50), Image.ANTIALIAS)
        self.img_fverde = ImageTk.PhotoImage(self.img_fverde)

        self.img_froja = Image.open("View/images/jugadores/rojo.png").resize((30,50), Image.ANTIALIAS)
        self.img_froja = ImageTk.PhotoImage(self.img_froja)

        self.fazul1 = self.canvas.create_image((110, 90), image=self.img_fazul)
        self.fazul2 = self.canvas.create_image((110, 150), image=self.img_fazul)
        self.fazul3 = self.canvas.create_image((70, 90), image=self.img_fazul)
        self.fazul4 = self.canvas.create_image((70, 150), image=self.img_fazul)

        self.famarillo1 = self.canvas.create_image((110, 690), image=self.img_famarillo)
        self.famarillo2 = self.canvas.create_image((110, 750), image=self.img_famarillo)
        self.famarillo3 = self.canvas.create_image((70, 690), image=self.img_famarillo)
        self.famarillo4 = self.canvas.create_image((70, 750), image=self.img_famarillo)

        self.fverde1 = self.canvas.create_image((710, 90), image=self.img_fverde)
        self.fverde2 = self.canvas.create_image((710, 150), image=self.img_fverde)
        self.fverde3 = self.canvas.create_image((670, 90), image=self.img_fverde)
        self.fverde4 = self.canvas.create_image((670, 150), image=self.img_fverde)

        self.froja1 = self.canvas.create_image((710, 690), image=self.img_froja)
        self.froja2 = self.canvas.create_image((710, 750), image=self.img_froja)
        self.froja3 = self.canvas.create_image((670, 690), image=self.img_froja)
        self.froja4 = self.canvas.create_image((670, 750), image=self.img_froja)

        self.dados = Button(self.window, text = "Lanzar dados", width = 8, height = 2, command = lambda: self.update_turno())
        self.dados.place(x=15, y=880)

    def render(self):
        '''
        Render basico del tablero
        '''
        self.window.mainloop()
    
    def update_turno(self):
        '''
        Imprime visualmente turnos y dados
        '''
        self.controller.movimiento()
        self.string_turno.set("Turno: " + str(self.controller.get_turno_str()))
        self.label_turno.configure(text=self.string_turno.get())
        self.string_dados.set("Dados: " + str(self.controller.get_dados_int()))
        self.label_dados.configure(text=self.string_dados.get())

    def sacar_carcel(self, jugador):
        '''
        Imprime visualmente turnos y dados
        Args:
            jugador: array
        '''
        if jugador[0][3] == "0001":
            self.delete_canvas([self.fazul1,self.fazul2,self.fazul3,self.fazul4])
            self.fazul1 = self.canvas.create_image((260, 140), image=self.img_fazul) # +x:derecha  -y: sube
            self.fazul2 = self.canvas.create_image((290, 140), image=self.img_fazul)
            self.fazul3 = self.canvas.create_image((310, 140), image=self.img_fazul)
            self.fazul4 = self.canvas.create_image((340, 140), image=self.img_fazul)
        if jugador[0][3] == "0002":
            self.delete_canvas([self.famarillo1,self.famarillo2,self.famarillo3,self.famarillo4])
            self.famarillo1 = self.canvas.create_image((150, 440), image=self.img_famarillo)# +x:derecha  -y: sube
            self.famarillo2 = self.canvas.create_image((150, 470), image=self.img_famarillo)
            self.famarillo3 = self.canvas.create_image((150, 500), image=self.img_famarillo)
            self.famarillo4 = self.canvas.create_image((150, 530), image=self.img_famarillo)
        if jugador[0][3] == "0003":
            self.delete_canvas([self.fverde1,self.fverde2,self.fverde3,self.fverde4])
            self.fverde1 = self.canvas.create_image((650, 235), image=self.img_fverde)# +x:derecha  -y: sube
            self.fverde2 = self.canvas.create_image((650, 265), image=self.img_fverde)
            self.fverde3 = self.canvas.create_image((650, 295), image=self.img_fverde)
            self.fverde4 = self.canvas.create_image((650, 325), image=self.img_fverde)
        if jugador[0][3] == "0004":
            self.delete_canvas([self.froja1,self.froja2,self.froja3,self.froja4])
            self.froja1 = self.canvas.create_image((470, 650), image=self.img_froja)# +x:derecha  -y: sube
            self.froja2 = self.canvas.create_image((500, 650), image=self.img_froja)
            self.froja3 = self.canvas.create_image((530, 650), image=self.img_froja)
            self.froja4 = self.canvas.create_image((560, 650), image=self.img_froja)
    
    def meter_carcel(self, jugador):
        if jugador[3] == "0001":
            self.delete_canvas([self.fazul1,self.fazul2,self.fazul3,self.fazul4])
            self.fazul1 = self.canvas.create_image((110, 90), image=self.img_fazul)
            self.fazul2 = self.canvas.create_image((110, 150), image=self.img_fazul)
            self.fazul3 = self.canvas.create_image((70, 90), image=self.img_fazul)
            self.fazul4 = self.canvas.create_image((70, 150), image=self.img_fazul)
        if jugador[3] == "0002":
            self.delete_canvas([self.famarillo1,self.famarillo2,self.famarillo3,self.famarillo4])
            self.famarillo1 = self.canvas.create_image((110, 690), image=self.img_famarillo)
            self.famarillo2 = self.canvas.create_image((110, 750), image=self.img_famarillo)
            self.famarillo3 = self.canvas.create_image((70, 690), image=self.img_famarillo)
            self.famarillo4 = self.canvas.create_image((70, 750), image=self.img_famarillo)
        if jugador[3] == "0003":
            self.delete_canvas([self.fverde1,self.fverde2,self.fverde3,self.fverde4])
            self.fverde1 = self.canvas.create_image((710, 90), image=self.img_fverde)
            self.fverde2 = self.canvas.create_image((710, 150), image=self.img_fverde)
            self.fverde3 = self.canvas.create_image((670, 90), image=self.img_fverde)
            self.fverde4 = self.canvas.create_image((670, 150), image=self.img_fverde)
        if jugador[3] == "0004":
            self.delete_canvas([self.froja1,self.froja2,self.froja3,self.froja4])
            self.froja1 = self.canvas.create_image((710, 690), image=self.img_froja)
            self.froja2 = self.canvas.create_image((710, 750), image=self.img_froja)
            self.froja3 = self.canvas.create_image((670, 690), image=self.img_froja)
            self.froja4 = self.canvas.create_image((670, 750), image=self.img_froja)

    def update_tablero(self, jugador, c_logica):
        print('Tablero.py: Pos recibida:' + str(c_logica))
        dicc_positions = { #Coordenada logica (y,x) - Coordenada visual (x,y)
            (7,0):(300,0),#(x,y) #Bien ubicado
            (7,1):(300,20),
            (7,2):(300,70), # #Bien ubicado
            (7,3):(300,100), # 
            (7,4):(300,120), #Bien ubicado
            (7,5):(300,170), # 
            (7,6):(270,190), #Bien ubicado
            (7,7):(270,240),#1 Coordenadas especiales: aca se hacen dos movimientos Bien ubicado
            (6,7):(220,270), #Bien ubicado
            (5,7):(180,270),
            (4,7):(150,270), # Bien ubicado
            (3,7):(110,270),
            (2,7):(80,270), # Bien ubicado
            (1,7):(50,270), #
            (0,7):(15,310),#2 #Bien ubicado
            (0,8):(15,400), 
            (0,9):(15,480),#3 #Bien ubicado
            (1,9):(50,480),
            (2,9):(85,480), #Bien ubicado
            (4,9):(150,480), # #Bien ubicado
            (3,9):(120,480), # #Bien ubicado
            (5,9):(180,480),
            (6,9):(220,480), # Bien ubicado
            (7,9):(270,525),#4 Coordenadas especiales: aca se hacen dos movimientos 
            (7,10):(290,570), # Bien ubicado
            (7,11):(300,600),
            (7,12):(300,640), # Bien ubicado
            (7,13):(300,670), #Bien ubicado
            (7,14):(300,700), #Bien ubicado
            (7,15):(300,735), #Bien ubicado
            (7,16):(300,760),#5 #Bien ubicado
            (8,16):(380,770), 
            (9,16):(500,760),#6 Bien ubicado
            (9,15):(500,730),
            (9,14):(500,700), #Bien ubicado
            (9,13):(500,660),
            (9,12):(500,630), # Bien ubicado
            (9,11):(500,600), #
            (9,10):(500,570), #Bien ubicado
            (9,9):(550,550),#7 Coordenadas especiales: aca se hacen dos movimientos 
            (10,9):(580,480), #Bien ubicado
            (11,9):(620,480),
            (12,9):(650,480), #Bien ubicado
            (13,9):(690,480),
            (14,9):(715,480), #Bien ubicado
            (15,9):(750,480),  #Bien ubicado
            (16,9):(780,480),#8 #Bien ubicado
            (16,8):(780,360),
            (16,7):(780,300),#9 #Bien ubicado
            (15,7):(740,300), #
            (14,7):(715,300), ##Bien ubicado
            (13,7):(690,300),
            (12,7):(655,300),#Bien ubicado
            (11,7):(580,300), #
            (10,7):(580,280), #Bien ubicado
            (9,7):(540,240),#10 Coordenadas especiales: aca se hacen dos movimientos 
            (9,6):(500,190), #Bien ubicado
            (9,5):(500,160),#Bien ubicado
            (9,4):(500,130),#Bien ubicado
            (9,3):(500,100), #Bien ubicado
            (9,2):(500,65),#Bien ubicado
            (9,1):(500,40), #Bien ubicado
            (9,0):(500,10),#11 #Bien ubicado
            (8,0):(400,0),  #Bien ubicado
        }   
        if jugador[0][3] == "0001":
            self.delete_canvas([self.fazul1,self.fazul2,self.fazul3,self.fazul4])
            self.fazul1 = self.canvas.create_image(dicc_positions[c_logica], image=self.img_fazul) # +x:derecha  -y: sube
        if jugador[0][3] == "0002":
            self.delete_canvas([self.famarillo1,self.famarillo2,self.famarillo3,self.famarillo4])
            self.famarillo1 = self.canvas.create_image(dicc_positions[c_logica], image=self.img_famarillo) # +x:derecha  -y: sube
        if jugador[0][3] == "0003":
            self.delete_canvas([self.fverde1,self.fverde2,self.fverde3,self.fverde4])
            self.fverde1 = self.canvas.create_image(dicc_positions[c_logica], image=self.img_fverde) # +x:derecha  -y: sube
        if jugador[0][3] == "0004":
            self.delete_canvas([self.froja1,self.froja2,self.froja3,self.froja4])
            self.froja1 = self.canvas.create_image(dicc_positions[c_logica], image=self.img_froja) # +x:derecha  -y: sube

    def get_render(self):
        '''
        Devuelve el window para renderizarlo en view.py
        '''
        return self.window
    
    def delete_canvas(self, data_delete):
        for data in data_delete:
            self.canvas.delete(data)