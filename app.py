from View.view import View
from Controller.controller import Controller
from Model.model import Model

class App():
    
    def __init__(self):
        '''
        Desde aca corre el juego, unica instanciacion del controlador, modelo y vista.
        '''
        self.controller = Controller()
        self.model = Model()
        self.view = View("Parqués", self.controller)

        self.model.set_controller(self.controller)
        self.controller.set_model(self.model)
        self.controller.set_view(self.view)

        self.view.render_start()
          
app = App()