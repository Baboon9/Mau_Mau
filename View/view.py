class View:
    def __init__(self, device):
        print("Viewport has been initialized.", "The selected device is:",type(device))
        self.device = device 

    def update(self,method, message, game):
        self.device.render(method, message, game)

class Console:
    
    def render(self, method, message, game):
        strbuffer = ""
        if method == "debug":
            strbuffer = strbuffer + self.debugMessage(message)
            
        elif method == "gameInfo":
            strbuffer = strbuffer + self.gameInfo(message)
        
        elif method == "printTopCard":
            strbuffer = strbuffer + self.printTopCard(game.deck)

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

    def printTopCard(self, deck):
        return str("The top card on the deck is: \n\t\t"+deck.deck[deck.getLen()-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            return str("Color: "+x.color+"Number: "+x.number)
    
    def printHand(self, hand):
        if hand.getHand() == []:
            print("ERROR: The starting hand has not been dealt yet")
            return "" 
        strbuffer = ""
        for x in hand.getHand():
            strbuffer = strbuffer + str("Player Hand Cards: \t"+x.asText()+"\t\t\t\n" )
        return strbuffer

