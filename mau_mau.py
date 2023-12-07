import random
import View.view as V
import Model.model as M
import Controller.controller as C


console=V.Console()
controller=C.Controller()
view=V.View(console)
model=M.Model(view, controller)
deck=M.Deck()
table_stack=M.TableStack()

#TODO make Deck a sigleton
#deck=M.Deck()
#So that the game can be played, it is important to 
#make make the cards appear on the table and shuffle them
#M.Deck.generate()
#M.Deck.shuffle()
#TODO Make TableStack a singleton
#table_stack=M.TableStack()
hand1 = M.Hand()
hand2 = M.Hand()
human_player=M.Player(False, hand1)
computer_player=M.Player(True, hand2)
#human_player.hand.pickInitialCards()
#computer_player.hand.pickInitialCards()
#M.TableStack.placeStartingCard(M.Deck.getInstance())
#must be standalone instance
#model.game.start()
#TODO Make Game a singleton
game=M.Game(deck,human_player,computer_player,table_stack)
game.start()

#running state
#notify view 

turncount = 0
while(game.game_state==game.getGameStates()[1]):
    turncount = turncount +1
    
    view.update("gameInfo", "\n#################################\nThis is the " + str(turncount) + "th turn", game)
    view.update("gameInfo", "There are " + str(deck.getLen()) + " Cards on the deck",game)
    view.update("gameInfo", "There are " + str(len(human_player.hand.getCards())) + " Cards on your Hand", game)
    view.update("gameInfo", "There are " + str(len(computer_player.hand.getCards())) + " Cards on the computer players Hand", game)
    view.update("printTopCard", None, game)
    view.update("printHand",None,game)
    view.update("gameInfo", "\nPick a card!\n################################", game)
    

    input = controller.update(console)

    if input in ["exit", "quit","break","q"]:
        break
   
    try:
        selectedCard = human_player.hand.getCards()[int(input)]
    except:
        selectedCard = human_player.hand.getCards()[0]
    finally:
        print("ERROR: The selected card can not be found.")
    
    if selectedCard == None:
        selectedCard=0


    isMatching = game.checkMatchingCard(selectedCard, table_stack)
    
    if isMatching:
        view.update("gameInfo","The Card is matching!", game)
        human_player.hand.dropACard(selectedCard, table_stack)
    else:
        view.update("gameInfo","The Card is not matching!\n", game)
        human_player.pickUpACard(deck)

    
    computer_can_drop = False
    for card in computer_player.hand.getCards():
        if game.checkMatchingCard(card, table_stack):
            computer_can_drop = True

    if computer_can_drop:
        computer_player.dropACard(card, table_stack)
    else:
        computer_player.hand.pickUpACard(deck)
    
    if human_player.hand.getLen() == 0 or computer_player.hand.getLen() == 0:
        game.gameOver()

    if game.getGameStates==game.getGameStates()[4]:
        view.update("\n\n\ngameInfo", "GAME OVER\n", game)
