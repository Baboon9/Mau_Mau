class View:
    def __init__(self):
        self.console = Console()
        self.console.debugMessage("View Class has been initialized")
   
    def update(self):
        pass 

class Console:
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


