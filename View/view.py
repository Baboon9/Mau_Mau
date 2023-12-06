class View:
    def __init__(self, device):
        self.device = device 

    def update(device, method, message, game):
        device.render(method, message, game)

class Console:
    
    def render(self, method, message, game):
        if method == "debug":
            self.debugMessage(message)
            
        if method == "printTopCard":
            self.printTopCard(game.deck)

        if method == "printDeck":
            self.printDeck(game.deck)

        if method == "printHand":
            self.printHand(game.player.hand)

    def debugMessage(self, message):
        return str("DEBUG:",message)

    def __init__(self):
        pass

    def printTopCard(self, deck):
        return str("The top card on the deck is: \n\t\t", deck[len(self.deck)-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            return str("Color: ",x.color,"Number: ",x.number)
    
    def printHand(self, hand):
        for x in hand:
            return str("Player Hand Cards: \t", x.asText() + "\t\t",  hand.index(x), "\t" )


