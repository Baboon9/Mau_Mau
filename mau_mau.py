import random
import View.view as V
import Model.model as M
import Controller.controller as C


console=V.Console()

model=M.Model()
view=V.View(mode="GUI")
controller=C.Controller(model, view)

controller.config_GUI()
controller.create_GUIlayout()
controller.create_GUI()
controller.run_GUI()

"""
turncount = 0
while(game.game_state==game.getGameStates()[1]):
    turncount = turncount +1
""" 
    #view.update("gameInfo", "\n#################################\nThis is the " + str(turncount) + "th turn", game)
    #view.update("gameInfo", "There are " + str(deck.getLen()) + " Cards on the deck",game)
    #view.update("gameInfo", "There are " + str(len(human_player.hand.getCards())) + " Cards on your Hand", game)
    #view.update("gameInfo", "There are " + str(len(computer_player.hand.getCards())) + " Cards on the computer players Hand", game)
    #view.update("printTopCard", None, game)
    #view.update("printHand",None,game)
    #view.update("gameInfo", "\nPick a card!\n################################", game)
    
"""
    input = controller.read_input()

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

"""
