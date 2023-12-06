class View:
    def __init__(self):
        self.console = Console()

class Console:
    def __init__(self):
        pass

    def printHand(self):
        pass

    def printTopCard(self, deck):
        print("The top card on the deck is: \n\t\t", deck[len(self.deck)-1].asText() )


    def printDeck(self, deck):
        for x in deck:
            print("Color: ",x.color,"Number: ",x.number)
