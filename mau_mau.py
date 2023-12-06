import random
import View.view
import Model.model
import Controller.controller


controller=Controller.controller.Controller()
view=View.view.View()
model=Model.model.Model(view, controller)
     

#moved to model
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

#moved to model
class Player:
    def __init__(self, computer):
        self.computer = computer
        self.deck = Deck()
        self.hand = []

    def pickUpACard(self, deck):
        self.hand.append(deck.pickOneCard())

    def pickInitialCards(self, deck):
        for i in range(0,7):
            self.pickUpACard(deck)

    def printHand(self):
        for x in self.hand:
            print("Player Hand Cards: \t", x.asText() + "\t\t",  self.hand.index(x), "\t" )


class Deck:
    def __init__(self):
        pass

    #moved to model
    def generateDeck(self):
        self.deck = []
        for i in range (0,12):
            for j in range (0,3):
                self.deck.append(Card(j, i))
        
        return self.deck

    #mved to view
    def printDeck(self):
        for x in self.deck:
            print("Color: ",x.color,"Number: ",x.number)

    #moved to model    
    def shuffle(self):
        random.shuffle(self.deck)

    #moved to model
    def pickOneCard(self):
        try:
            picked_card = self.deck.pop()
        except:
            print("The Deck is empty")
            self.generateDeck()
            picked_card = self.deck.pop()
        finally:
            return picked_card
    
    #moved to view
    def printTopCard(self):
        print("The top card on the deck is: \n\t\t", self.deck[len(self.deck)-1].asText() )

#moved to model
class Game:
    def __init__(self):
        self.game_states = ["initializing", "running", "stopped", "over", "new"]
        self.game_state = self.game_states[0]
        self.deck = Deck()
        self.deck.generateDeck()
        self.deck.shuffle()
        self.human_player = Player(False)
        self.human_player.pickInitialCards(self.deck)
        self.computer_player = Player(True)
        self.computer_player.pickInitialCards(self.deck)
        
        self.table_stack = []
        self.table_stack.append(self.deck.pickOneCard())

        self.newGame()

    #moved to model
    def checkMatchingCard(self, card):
        if card.number == self.table_stack[-1].number or card.color == self.table_stack[-1].color:
            return True
        else:
            return False
    
    #moved to model
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
            


            card_found = False
            for x in self.computer_player.hand:
                if self.checkMatchingCard(x):
                    self.table_stack.append(self.computer_player.hand.pop(self.computer_player.hand.index(x)))
                    card_found = True
                    break
            if not card_found:
                self.computer_player.pickUpACard(self.deck)

            print("The computer player has ",len(self.computer_player.hand), "Cards on his hand.")

            print("Next turn!\n##########")

            if len(self.human_player.hand) == 0 or len(self.computer_player.hand) == 0:
                print("Okay, game is over! Well played! Good game!")
                self.game_state = self.game_states[2]
                self.gameOver()

    #moved to model
    def stop(self):
        pass
    
    #moved to model
    def gameOver(self):
        print("This was a triumph, I making a note here, huge success..\n\nCredits: Tim-Ohle Schürheck\nThanks for playing!")

    #moved to model
    def newGame(self):
        self.game_state = self.game_states[4]
        print("New Game Has started!")
        self.run()


