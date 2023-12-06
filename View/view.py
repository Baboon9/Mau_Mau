class View:
    def __init__(self):
        self.console = Console()

class Console:
    def __init__(self):
        pass

    def printTopCard(self, deck):
        print("The top card on the deck is: \n\t\t", deck[len(self.deck)-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            print("Color: ",x.color,"Number: ",x.number)
    
    def printHand(self, hand):
        for x in hand:
            print("Player Hand Cards: \t", x.asText() + "\t\t",  hand.index(x), "\t" )
