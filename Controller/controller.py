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

    def update_GUI(self):
        self.view.get_GUI().update_interface(self.model.get_game(), self.model)

    def bind_tableStack(self):
        self.view.get_GUI().get_lbl_deck().bind("<Button-1>", self.clicked_deck)
    
    def bind_humanPlayerCards(self):
        hand = self.view.get_GUI().get_lbl_humanHand()
        for card in hand:
            card.bind("<Button-1>", self.clicked_card)

    def clicked_card(self, event):
        print(event.widget)

    def clicked_deck(self, event):
        self.model.get_humanPlayer().pick_card(self.model.get_deck())
        self.view.get_GUI().update_interface(self.model.get_game(), self.model)
        self.bind_humanPlayerCards()
