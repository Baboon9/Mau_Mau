import tkinter as tk
from tkinter import ttk
import sys

class View:
    _device = None
    _model = None
    def setModel(self, model):
        self.model = model

    def __init__(self, device):
        self._device = device 

    def update(self,method, message, game):
        self._device.render(method, message, game)

class GUI(tk.Tk):
   
    def close(self, event):
        self.withdraw()
        sys.exit()

    def setModel(self,model):
        self.model=model

    def run(self):
        self.mainloop()

    def config(self):
        self.title="MauMau"
        self.geometry("860x600+100+100")
        self.resizable(False, False)
        self.configure(background="#000")
        self.bind('<Escape>', self.close)

    def __init__(self):
        super().__init__()
        self.config()

    def render(self):
        pass

    def build_GUI(self):

        self.width=860
        self.height=600
        self.card_height=200

        self.lbl_deck=ttk.Label(self, text="?", padding=(10,10,self.card_height/2-3,150), background='#ff2')
        self.lbl_deck.grid( column=0,row=1, padx=3, pady=3)

        self.lbl_table_stack=ttk.Label(self, text="to set", padding=(10,10,self.card_height/2-23,150))
        self.lbl_table_stack.grid( column=1,row=1, padx=3, pady=3)

        self.lbl_computerHand=[]

        self._lbl_comp_hand=[]

        comp_cards = self.model.getComputerPlayer().getHand().getCards()
        for card in comp_cards: 
            label = ttk.Label(self, text="X",padding=(10, 10, self.card_height/2-3, 150))
            self._lbl_comp_hand.append(label)
        
        for lbl in self._lbl_comp_hand:
            lbl.grid(row=0, column=self._lbl_comp_hand.index(lbl), padx=3, pady=3)
  

        self._btn_human_hand=[]
        player_cards = self.model.getHumanPlayer().getHand().getCards()
        
        for card in player_cards:
            button = ttk.Button(self, text="???", padding=(10,10,self.card_height/2-3,150))  
            self._btn_human_hand.append(button)

        for btn in self._btn_human_hand:
            btn.grid(row=2, column=self._btn_human_hand.index(btn), padx=3, pady=3)
        

class Console:
    
    def render(self, method, message, game):
        strbuffer = ""
        if method == "debug":
            strbuffer = strbuffer + self.debugMessage(message)
            
        elif method == "gameInfo":
            strbuffer = strbuffer + self.gameInfo(message)
        
        elif method == "printTopCard":
            strbuffer = strbuffer + self.printTopCard(game.table_stack)

        elif method == "printDeck":
            strbuffer = strbuffer + self.printDeck(game.deck)

        elif method == "printHand":
            strbuffer = strbuffer + self.printHand(game.human_player.hand)
        else:
            strbuffer = strbuffer + self.debugMessage("WARNING: Wrong message identifyer")
        
        print(strbuffer)

    def debugMessage(self, message):
        return str("DEBUG:"+message)

    def __init__(self):
        pass

    def gameInfo(self, message):
        return message

    def printTopCard(self, table_stack):
        return str("The top card on the table is: \n\t\t"+table_stack.getCards()[table_stack.getLen()-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            return str("Color: "+x.color+"Number: "+x.number)
    
    def printHand(self, hand):
        if hand.getCards() == []:
            print("ERROR: The starting hand has not been dealt yet")
            return "" 
        strbuffer = ""
        for x in hand.getCards():
            strbuffer = strbuffer + str("Player Hand Cards: \t"+x.asText()+"\t\t"+str(hand.getCards().index(x))+"\t\n" )
        return strbuffer

