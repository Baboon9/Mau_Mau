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
        
        #When we want to play a game of Mau Mau we have to have at least 2 players
        #And then when the game starts they have to get their initial cards on their hands
        self.human_player = Player(False)
        self.human_player.pickInitialCards(self.deck)
        self.computer_player = Player(True)
        self.computer_player.pickInitialCards(self.deck)
        
        #When the game is initialized it needs a stack of cards on the table for placing handcards
        #This should actually be a class on its own
        #TODO: Make this a class on its own
        self.table_stack = []
        self.table_stack.append(self.deck.pickOneCard())
        
        self.game.newGame()

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

        #moved to model
        #self.human_player = Player(False)
        #self.human_player.pickInitialCards(self.deck)
        #self.computer_player = Player(True)
        #self.computer_player.pickInitialCards(self.deck)
        
        #moved to model
        #self.table_stack = []
        #self.table_stack.append(self.deck.pickOneCard())

        #self.newGame()

    #When the game is running and the turn has begun there has to be cards compared 
    #No card can be placed on the stack that does not match at least the color or the number of that given card
    def checkMatchingCard(self, card):
        if card.number == self.table_stack[-1].number or card.color == self.table_stack[-1].color:
            return True
        else:
            return False


    #Main game loop
    def run(self):
        self.game_state = self.game_states[1]
        while self.game_state == "running":
            print("The top card on the table stack is:")
            print("\n",self.table_stack[-1].asText())
            print()
            self.human_player.printHand()
            print("")
            picked_card = input("Select a card you want to put on the open table stack..")
            
            
            print()
            print()
            
            try:
                if self.checkMatchingCard(self.human_player.hand[int(picked_card)]):
                    print("Okay, these cards do match!")
                    print("Removing selected Card form players Hand and putting it on the table stack..\n")
                    self.table_stack.append(self.human_player.hand.pop(int(picked_card)))

                else:
                    print("No! These cards do NOT match!")
                    print("Select another card!! Or pass by pressing Enter")

            except:
                self.human_player.pickUpACard(self.deck) 

            print("Alright, now its the computer players turn!")
            print("###########################################")
            
    
    def stop(self):
        pass
    
    #end the game and show credits
    def gameOver(self):
        print("This was a triumph, I making a note here, huge success..\n\nCredits: Tim-Ohle Schürheck\nThanks for playing!")

    #start a new game
    def newGame(self):
        self.game_state = self.game_states[4]
        print("New Game Has started!")
        self.run()


class Player:
    def __init__(self):
        pass

class Hand:
    def __init__(self):
        pass


