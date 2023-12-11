import tkinter as tk


class View:
    def __init__(self, device):
        self.device = device 

    def update(self,method, message, game):
        self.device.render(method, message, game)

class GUI:
    _root = tk.Tk()
    def __init__(self):
        pass

    def run(self):
        self._root.mainloop()
    

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

