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
            
        elif method == "printTopCard":
            strbuffer = strbuffer + self.printTopCard(game.deck)

        elif method == "printDeck":
            strbuffer = strbuffer + self.printDeck(game.deck)

        elif method == "printHand":
            strbuffer = strbuffer + self.printHand(game.player.hand)
        else:
            strbuffer = strbuffer + self.debugMessage("WARNING: Wrong message identifyer")
        
        print(strbuffer)

    def debugMessage(self, message):
        return str("DEBUG:"+message)

    def __init__(self):
        pass

    def printTopCard(self, deck):
        return str("The top card on the deck is: \n\t\t"+deck[len(self.deck)-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            return str("Color: "+x.color+"Number: "+x.number)
    
    def printHand(self, hand):
        for x in hand:
            return str("Player Hand Cards: \t"+x.asText()+"\t\t"+hand.index(x)+"\t" )


