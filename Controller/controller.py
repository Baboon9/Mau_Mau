import View.view 

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def read_input(self):
        pass
   
    def create_GUI(self):
        self.view.get_GUI().create_GUI(self.model)

    def run_GUI(self):
        self.view.get_GUI().run()
    
    def config_GUI(self):
        self.view.get_GUI().config()

    def create_GUIlayout(self):
        self.view.get_GUI().create_layout()
