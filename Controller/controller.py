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
    

    #TODO:
    #View needs to be update
    def clicked_card(self, event):
        gui = self.view.get_GUI()
        human_hand_widget = gui.get_lbl_humanHand()
        index = human_hand_widget.index(event.widget)
        human_player = self.model.get_humanPlayer()
        human_player_cards = human_player.get_hand().get_cards()
        selected_card = human_player_cards[index]
        game = self.model.get_game()
        isMatching = game.check_matchingCard(selected_card, 
                                             game.get_tableStack())
        deck = self.model.get_deck()

        if isMatching:
            human_player.drop_card(selected_card,
                                   self.model.get_tableStack())
           
            computer_player = self.model.get_game().get_computerPlayer()
            table_stack = self.model.get_tableStack()
            computer_can_drop = False

            for card in computer_player.hand.get_cards():
                if game.check_matchingCard(card, table_stack):
                    computer_can_drop = True
                    print("computer can drop")

                if computer_can_drop:
                    computer_player.drop_card(card, table_stack)
                    print("computer has dropped")
                    break
            
            if not computer_can_drop:
                computer_player.hand.pick_card(deck)
            
            gui.update_interface(game, self.model)


        self.bind_humanPlayerCards()

    #When the Deck has been clicked a card will be added to the human Players Hand.
    #The GUI will then partially be rebuild, so that the new card will be displayed.
    #Every Card will then get an Eventlistener again.
    def clicked_deck(self, event):
        self.model.get_humanPlayer().pick_card(self.model.get_deck())
        self.view.get_GUI().update_interface(self.model.get_game(), self.model)
        self.bind_humanPlayerCards()
