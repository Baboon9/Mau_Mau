import tkinter as tk
from tkinter import ttk
import sys

class View:
    pass

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
        self.configure(background="#333")
        self.bind('<Escape>', self.close)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def __init__(self):
        super().__init__()
        self.config()
        self.create_layout()
        #self.create_GUI()

    def update_interface(self, game):
        table_stack = game.getTableStack()
        
        self.lbl_table_stack.configure(text='Color:\n  ' + table_stack.getCards()[-1].getColor()+'\nNumber:\n  ' + table_stack.getCards()[-1].getNumber())

        player_cards = game.getHumanPlayer().getHand().getCards()
        for i in range(len(player_cards)):
            self._btn_human_hand[i].configure(text='Color:\n  '+player_cards[i].getColor()+'\nNumber:\n  '+player_cards[i].getNumber(), background='#fff')

            

    def render(self):
        pass

    def create_layout(self):
        self.top_frame=tk.Frame(self)
        self.middle_frame=tk.Frame(self)
        self.bottom_frame=tk.Frame(self)
        self.top_frame.configure(borderwidth=5,relief='solid', height=200, width=860, bg='#222' )
        self.middle_frame.configure(borderwidth=5, height=200, width=860,bg='#333')
        self.bottom_frame.configure(borderwidth=5,relief='solid', height=200, width=860, bg='#444') 
        self.top_frame.grid(row=0, column=0, sticky='EW')
        self.middle_frame.grid(row=1, column=0, sticky='EW')
        self.bottom_frame.grid(row=2, column=0, sticky='EW') 
    
    def create_card(self, frame):
        card = ttk.Label(frame, text="COLOR: \nXXXXXXX\nNUMBER: \nXXXXXXX", background='#aaa', padding=(10,10,10,140), relief='solid', font='courir')
        return card


    def create_GUI(self):

        self.width=860
        self.height=600
        self.card_height=200
        
        card_properties=None
        
        self.lbl_deck=self.create_card(self.middle_frame)
        self.lbl_deck.grid(row=0, column=0, padx=3, pady=3)
        self.lbl_deck.configure(text='??????\n\n\n', background='#faf')
        self.lbl_table_stack=self.create_card(self.middle_frame)
        self.lbl_table_stack.grid(row=0, column=1, padx=3, pady=3)
        self.lbl_table_stack.configure(background='#eff')
        self.lbl_computerHand=[]

        self._lbl_comp_hand=[]

        comp_cards = self.model.getComputerPlayer().getHand().getCards()
        for card in comp_cards: 
            label = self.create_card(self.top_frame) 
            label.configure(text='XXXXX\n\n\n')
            self._lbl_comp_hand.append(label)
        
        for lbl in self._lbl_comp_hand:
            lbl.grid(row=0, column=self._lbl_comp_hand.index(lbl), padx=3, pady=3)
  

        self._btn_human_hand=[]
        player_cards = self.model.getHumanPlayer().getHand().getCards()
        
        for card in player_cards:
            button = self.create_card(self.bottom_frame) 
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

