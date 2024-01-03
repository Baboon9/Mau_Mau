import random
import abc 

class GameInterface(object):
    __metaclass__=abc.ABCMeta
    _game_states=["initialization",
                  "setup",
                  "stopped",
                  "started",
                  "stopped",
                  "over",
                  "new"]

    def setup(self):
        return 

    def start(self):
        return
    
    def stop(self):
        return

    def over(self):
        return

    def initialize(self):
        return

    def new(self):
        return 

class Model:

    def get_humanPlayer(self):
        return self._human_player

    def get_computerPlayer(self):
        return self._computer_player

    def get_deck(self):
        return self._deck

    def __init__(self):
        self._table_stack=TableStack()
        self._deck=Deck()
        self._deck.generate()
        self._deck.shuffle()
        self._table_stack.place_startingCard(self._deck)
        self._hand1 = Hand()
        self._hand2 = Hand()
        self._human_player=Player(False, self._hand1)
        self._human_player.pick_initialCards(self._deck)
        self._computer_player=Player(True, self._hand2)
        self._computer_player.pick_initialCards(self._deck)
        self._game=Game(self._deck,self._human_player,self._computer_player,self._table_stack)
    
    def get_game(self):
        return self._game

class TableStack:
    def get_len(self):
        return len(self.cards)
    def get_cards(self):
        return self.cards
    def __init__(self):
        self.cards = []
    def place_startingCard(self, deck):
        self.cards.append(deck.pick_card())

class Deck:
    _instance=None
    _deck=[]
    def __init__(self):
        self.instance=TableStack()
        self.generate()
        self.shuffle()

    def get_instance(self):
        return self._instance

    def get_deck(self):
        return self._deck

    def get_len(self):
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
    def pick_card(self):
        try:
            picked_card = self._deck.pop()
        except:
            self.generate()
            picked_card = self._deck.pop()
        finally:
            return picked_card

class Game(GameInterface):
    
    def get_tableStack(self):
        return self.table_stack

    def get_humanPlayer(self):
        return self.human_player

    def get_gameStates(self):
        return self._game_states

    def set_humanPlayer(self, player):
        self.human_player=player

    def set_computerPlayer(self,player):
        self.computer_player=player
   
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
    def check_matchingCard(self, card, table_stack):
        if card.number == table_stack.get_cards()[-1].number or card.color == table_stack.get_cards()[-1].color:
            return True
        else:
            return False
    
    def start(self):
        self.game_state=self._game_states[1]
        self.human_player.pick_initialCards(self.deck)
        self.computer_player.pick_initialCards(self.deck)
        self.table_stack.place_startingCard(self.deck)
    
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

    def get_len(self):
        return len(self.cards)

    def get_cards(self):
        return self.cards

    def pick_initialCards(self, deck):
        for i in range(0,7):
            self.pick_card(deck)

    def drop_card(self, card, table_stack):
        dropped_card = card 
        dropped_card_index = self.cards.index(dropped_card)
        self.cards.pop(dropped_card_index)
        table_stack.get_cards().append(dropped_card)

    def pick_card(self, deck):
        self.cards.append(deck.pick_card())

class Player:
    def __init__(self, computer, hand):
        self.computer = computer
        #self.deck = Deck()
        self.hand = hand
    def pick_initialCards(self,deck):
        self.hand.pick_initialCards(deck)

    def pick_card(self, deck):
        self.hand.pick_card(deck)

    def get_hand(self):
        return self.hand

    def drop_card(self, card, table_stack):
        self.hand.drop_card(card, table_stack)

class Card:
    def get_number(self):
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
        return text_number

    def get_color(self):
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
        return text_color 

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
