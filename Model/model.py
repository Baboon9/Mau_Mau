import random

class Model:
    def __init__(self):
        self.game = Game()
        self.deck = Deck()
        self.players = []
        self.hands = []
        
        #So that the game can be played, it is important to 
        #make make the cards appear on the table and shuffle them
        self.deck.generate()
        self.deck.shuffle()


class Deck:
    def __init__(self):
        pass
    
    #So that the game can be played it has to have a deck of cards which are to use
    #for playing the game. These cards must be somehow be put on the table. 
    def generate(self):
        self.deck = []
        for i in range (0,12):
            for j in range (0,3):
                self.deck.append(Card(j, i))
        
        return self.deck

    #This is a helper function that allows the program to reuse the cards that have been generated
    def shuffle(self):
        random.shuffle(self.deck)

    #When the player is lacking the posiblity to play a card, he has to pick another one from the stack on the table
    def pickOneCard(self):
        try:
            picked_card = self.deck.pop()
        except:
            print("The Deck is empty")
            self.generateDeck()
            picked_card = self.deck.pop()
        finally:
            return picked_card

class Game:
    #When the game starts an instace of the game calss will be created.
    #This instace has important attributes.
    def __init__(self):
        self.game_states = ["initializing", "running", "stopped", "over", "new"]
        self.game_state = self.game_states[0]
        
        #moved to Model
        #self.deck = Deck()
        #self.deck.generateDeck()
        #self.deck.shuffle()
        self.human_player = Player(False)
        self.human_player.pickInitialCards(self.deck)
        self.computer_player = Player(True)
        self.computer_player.pickInitialCards(self.deck)
        
        self.table_stack = []
        self.table_stack.append(self.deck.pickOneCard())

        self.newGame()

class Player:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass


