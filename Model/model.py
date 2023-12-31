import random

class Model:
    def __init__(self, view, controller):
        self.view = view
        self.controller = controller
        #moved to main
        #self.deck = Deck()
        #self.players = []
        #self.hands = []
        
        
        #moved to main
        #When we want to play a game of Mau Mau we have to have at least 2 players
        #And then when the game starts they have to get their initial cards on their hands
        #self.human_player = Player(False, Hand())
        #moved to hand class
        #self.human_player.pickInitialCards(self.deck)
        #self.computer_player = Player(True, Hand())
        #moved to hand class
        #self.computer_player.pickInitialCards(self.deck)
        
        #moved to main
        #self.human_player.hand.pickInitialCards(self.deck)
        #self.computer_player.hand.pickInitialCards(self.deck)


        #moved to main
        #When the game is initialized it needs a stack of cards on the table for placing handcards
        #This should actually be a class on its own
        #TODO: Make this a class on its own
        #self.table_stack = TableStack()
        #self.table_stack.placeStartingCard(self.deck)
        
        #moved to main
        #self.game = Game(self.deck, self.human_player, self.computer_player, self.table_stack)

        #needs to be invoked somewhere else!
        #self.game.newGame()
        

class TableStack:
    _instance=None
    def __init__(self):
        self._instance=TableStack()
    def getLen(self):
        return len(self.cards)
    def getCards(self):
        return self.cards
    def __init__(self):
        self.cards = []
    def placeStartingCard(self, deck):
        self.cards.append(deck.pickUpACard())

class Deck:
    _instance=None
    _deck=[]
    def __init__(self):
        self.instance=TableStack()
        self.generate()
        self.shuffle()

    def getInstance(self):
        return self._instance

    def getDeck(self):
        return self._deck

    def getLen(self):
        return len(self._deck)

    #So that the game can be played it has to have a deck of cards which are to use
    #for playing the game. These cards must be somehow be put on the table. 
    def generate(self):
        self._deck = []
        for i in range (0,12):
            for j in range (0,3):
                self._deck.append(Card(j, i))
        
        return self._deck

    #This is a helper function that allows the program to reuse the cards that have been generated
    def shuffle(self):
        random.shuffle(self._deck)

    #When the player is lacking the posiblity to play a card, he has to pick another one from the stack on the table
    def pickUpACard(self):
        try:
            picked_card = self._deck.pop()
        except:
            self.generate()
            picked_card = self._deck.pop()
        finally:
            return picked_card

class Game:
    _instance=None
    _game_states = ["initializing", "running", "stopped", "over", "new"]

    def getGameStates(self):
        return self._game_states

    def getInstance(self):
        return self._instance
    
    def setHumanPlayer(self, player):
        self.human_player=player

    def setComputerPlayer(self,player):
        self.computer_player=player
   
    def __init__(self, deck, table_stack):
        self._instance=Game(deck, table_stack)
        self.deck=deck
        self.table_stack=table_stack
        self.game_state = self._game_states[0]


    #When the game starts an instace of the game calss will be created.
    #This instace has important attributes.
    def __init__(self, deck, human_player, computer_player, table_stack):
        self.human_player = human_player
        self.table_stack = table_stack
        self.computer_player = computer_player
        self.game_state = self._game_states[0]
        self.deck = deck

    #When the game is running and the turn has begun there has to be cards compared 
    #No card can be placed on the stack that does not match at least the color or the number of that given card
    def checkMatchingCard(self, card, table_stack):
        if card.number == table_stack.getCards()[-1].number or card.color == table_stack.getCards()[-1].color:
            return True
        else:
            return False
    
    def start(self):
        self.game_state=self._game_states[1]
        self.human_player.pickInitialCards(self.deck)
        self.computer_player.pickInitialCards(self.deck)
        self.table_stack.placeStartingCard(self.deck)

    def stop(self):
        pass
    
    #end the game and show credits
    def gameOver(self):
        self.game_state=self._game_states[4]
        #print("This was a triumph, I making a note here, huge success..\n\nCredits: Tim-Ohle Schürheck\nThanks for playing!")

    #start a new game
    def new(self):
        print("New Game has started!")
        self.game_state = self._game_states[0]

class Hand:
    def __init__(self):
        self.cards = []

    def getLen(self):
        return len(self.cards)

    def getCards(self):
        return self.cards

    def pickInitialCards(self, deck):
        for i in range(0,7):
            self.pickUpACard(deck)

    def dropACard(self, card, table_stack):
        dropped_card = card 
        dropped_card_index = self.cards.index(dropped_card)
        self.cards.pop(dropped_card_index)
        table_stack.getCards().append(dropped_card)

    def pickUpACard(self, deck):
        self.cards.append(deck.pickUpACard())

class Player:
    def __init__(self, computer, hand):
        self.computer = computer
        #self.deck = Deck()
        self.hand = hand
    def pickInitialCards(self,deck):
        self.hand.pickInitialCards(deck)

    def pickUpACard(self, deck):
        self.hand.pickUpACard(deck)

    def dropACard(self, card, table_stack):
        self.hand.dropACard(card, table_stack)

class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def asText(self):
        text_number = ""
        if self.number < 9:
            text_number = str(self.number + 2)

        elif self.number == 11:
            text_number = "Ace"

        elif self.number == 10:
            text_number = "King"

        elif self.number == 9:
            text_number = "Queen"

        elif self.number == 8:
            text_number = "Jack"

        else:
            print("An unexpected Error occured")
        
        text_color = ""

        if self.color == 0:
            text_color = "Clubs"  
        elif self.color == 1:
            text_color = "Spades"
        elif self.color == 2:
            text_color = "Hearts"
        elif self.color == 3:
            text_color = "Diamonds"
        else:
            print("An unexpected Error occured")
            
        return text_number + " of " + text_color
