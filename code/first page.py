

from tkinter import*
from PIL import ImageTk, Image
from resizeimage import resizeimage
import os
import random
import copy

#Back Bone tkinter structure gotten from notes on graphichs
class backEnd(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event): pass
    def keyPressed(self, event): pass
    def timerFired(self): pass
    def init(self): pass
    
    def redrawAll(self): pass

    
    # Call app.run(width,height) to get your app started
    def run(self, width=1300, height=900):
        # create the root and the canvas
        root = Tk()
        
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()

        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
            self.canvas.update()

        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()

        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()

        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)

        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
            
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()
        print("Bye")
#######################################################################################################################
#Uno Game 
#######################################################################################################################
class UnoGame(backEnd):
    def init(self):
        self.mode = "start" 
        self.level = None
        self.numOfPlayers = 4 

    ###############################
    #Title and Help Screen
    ##############################
        self.background = UserInterace.loadBackground()
        self.gif = UserInterace.loadGIF()
        self.noFunctionsIMG = UserInterace.loadnoFunctionImage()
        self.functionsIMG = UserInterace.loadFunctionsImage()
        self.winningBackground = UserInterace.loadWinningBackground()
    ########################################
    #Game Images
    ########################################
        self.table = UserInterace.loadTable()
        self.players = UserInterace.loadPlayers()
        self.AIplayer1 = self.players[0]
        self.AIplayer2 = self.players[1]
        self.AIplayer3 = self.players[2]
        self.cards = Cards.loadImage()
        self.unoButton = UserInterace.loadUnoButton()
        self.winningFace = UserInterace.loadWinner()
        self.wars = UserInterace.loadWars()
        
    ###########################################
        self.option = None
        self.switched = False 
        self.switchesLeft = 3
        self.other = 0
        self.otherUser1 = False
        self.otherUser2 = False 
        self.otherUser3 = False
        
        self.playOrder = []
        for num in range(1,self.numOfPlayers+1):
            self.playOrder.append(num)
        self.turn = None 
        self.mistakeCount = 0
        self.pickColor = None 
        self.isPick2 = False
        self.isPick4 = False
        self.isReverse = False 
        self.isSkip = False 
        self.isWildCard = False
        self.playerTurn = True
        self.AIplayer1Turn = False
        self.AIplayer2Turn = False
        self.AIplayer3Turn = False 
        self.sayUno = False 
        self.tomUNO = False
        self.richardUNO = False
        self.harryUNO = False 
        self.legal = None 
        self.timerDelay = 0 
        self.winner = None
        self.winnerFace = None 
        self.going = None 
        self.back = None 
        self.moveMade = None 
        self.gameOver = False
        self.test = None 
        self.next = None 
        self.play = False 
        self.reverse = False
        self.pause = 0
        


    def mousePressed(self,event):
        if self.mode == "start": UnoGame.startmousePressed(self,event)
        if self.mode == "help": UnoGame.helpmousePressed(self,event)
        if self.mode == "option":UnoGame.optionmousePressed(self,event)
        if self.mode == "selection": UnoGame.selectionmousePressed(self,event)
        if self.mode == "game": UnoGame.gamemousePressed(self,event)
    def keyPressed(self,event):
        if self.mode=="start": UnoGame.startkeyPressed(self,event)
        if self.mode == "help": UnoGame.helpkeyPressed(self,event)
        if self.mode ==  "option": UnoGame.optionkeyPressed(self,event)
        if self.mode == "selection": UnoGame.selectionkeyPressed(self,event)
        if self.mode == "game": UnoGame.gamekeyPressed(self,event)
    def timerFired(self):
        if self.mode=="start": UnoGame.starttimerFired(self)
        if self.mode == "help": UnoGame.helptimerFired(self) 
        if self.mode == "option": UnoGame.optiontimerFired(self)
        if self.mode == "selection": UnoGame.selectiontimerFired(self)
        if self.mode == "game": UnoGame.gametimerFired(self)
    def redrawAll(self):
        if self.mode=="start": UnoGame.startredrawAll(self)
        if self.mode == "help": UnoGame.helpredrawAll(self)
        if self.mode == "option": UnoGame.optionredrawAll(self)
        if self.mode == "selection": UnoGame.selectionredrawAll(self)
        if self.mode == "game": UnoGame.gameredrawAll(self)

    ############################################################
    #Start Page 
    ###########################################################
    def startmousePressed(self,event):
        pass

    def startkeyPressed(self,event):
        if event.keysym=="h":
            self.mode = "help"
        

    def startredrawAll(self):
        self.canvas.create_rectangle(0,0,1300,900,fill="black")
        self.canvas.create_image(300,350, image = self.background)
        self.canvas.create_image(800,550, image = self.wars)
        self.canvas.create_text(750,75,text="Press 'h' To Go to Instructions Page",fill="white",font="Times 28 italic")
        self.canvas.create_text(150,750,text="Oluwafunmbi Jaiyeola",fill="white",font="Times 20 italic")


    def starttimerFired(self):
       pass

    ####################################
    # HELP MODE
    ####################################
    def helpmousePressed(self,event):
        pass

    def helpkeyPressed(self,event):
        if event.keysym=="p":
            self.mode = "option"

    def helpredrawAll(self):
        self.canvas.create_rectangle(0,0,1300,900,fill="red")
        self.canvas.create_text(400,75,text="How To Play",fill="black",font="Times 28 italic underline")
        self.canvas.create_text(150,125,text="Objective:",fill="black",font="Times 20 italic bold underline")
        self.canvas.create_text(450,155,text="The goal of the game is to get rid of all your cards before anyone else",
        fill="white",font="Times 18 italic")
        self.canvas.create_text(435,200,text="Rules (Similar to Traditional UNO but several differences):",fill="black",font="Times 20 italic bold underline")
        self.canvas.create_text(450,250,text="- Match the top card with either a card of the same number or color",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,300,text="- A Wild Card or A Wild Draw +4 can be placed on any card",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,350,text="- If you have no cards to play, you can click the deck to pick up  ",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,400,text="- If you picked a card your turn is forfeited",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,450,text="- A message would pop up to tell you when it is your turn",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,500,text="- When you are about to have one card left press the UNO button to indicate it",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,550,text="- If you dont say UNO you are succeptible to being caught by the computer and having to draw 2 cards",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,600,text="- NO STACKING CARDS, only one card can be placed per turn",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,650,text="- If a 7 of any color is placed on the deck all players must swap hands",fill="white",font="Times 16 italic")
        self.canvas.create_text(500,675,text="PRESS 'p' TO CONTINUE",fill="black",font="Times 24 italic bold")

    def helptimerFired(self):
        pass
        ####################################
    # SELECTION MODE
    ####################################
    def selectionmousePressed(self,event):
        pass

    def selectionkeyPressed(self,event):
        if event.keysym=="a":
            self.timerFiredDelay = 300
            self.mode = "game"
            self.level="easy"
        elif event.keysym=="b":
            self.timerFiredDelay = 300
            self.mode = "game"
            self.level="hard"
        elif event.keysym == "1":
            self.other = 1
            self.mode = "game"
            self.level = "easy"
        


    def selectionredrawAll(self):
        self.canvas.create_rectangle(0,0,1300,900,fill="black")
        self.canvas.create_image(650,500, image = self.gif)
        self.canvas.create_text(650,75,text="Press the corresponding key level of dificulty",fill="white",font="Helvetica 32  bold")
        self.canvas.create_text(650,225,text="Press a for an easy game against Chidinma, Konama and Ubong",fill="white",anchor = "center", font="Helvetica 24 italic ")
        self.canvas.create_text(650,350,text="Press b for a tough match against Chidinma, Konama and Ubong",fill="white",font="Helvetica 24 italic ")
        self.canvas.create_text(650,425, text = "Or,press 1 to allow for your friend to be added to the game", fill = "white", font = "Helverica 24 italic")


    def selectiontimerFired(self):
        if self.option == "noFunctions":
            for card in UnoDeck.deck:
                if card.kind == 12 or card.kind == 13 or card.kind == 14:
                	i = UnoDeck.deck.index(card)
                	UnoDeck.deck.pop(i)
            self.deck = UnoDeck.deck
        else:
        	self.deck = UnoDeck.deck
        self.deckFace = [self.deck[0]]
        self.picked = False
        ###########################################
    #Each players hand and starting card 
        self.playerHand = Hand.loadHand(UnoDeck.deck)
        self.AI1 = AI1Hand.loadHand(UnoDeck.deck)
        self.AI2 = AI2Hand.loadHand(UnoDeck.deck)
        self.AI3 = AI3Hand.loadHand(UnoDeck.deck)
        self.top = []
        self.top.append(UnoDeck.deck.pop(-1))
        
    ###########################################

    ###############################
    #Option Mode
    ###############################
    def optionmousePressed(self,event):
    	pass
    def optionkeyPressed(self,event):
        if event.keysym == "o":
            self.option = "noFunctions"
            self.mode = "selection"
        elif event.keysym == "O":
        	self.option = "addFunctions"
        	self.mode = "selection"
    def optiontimerFired(self):
    	pass
    def optionredrawAll(self):
        self.canvas.create_rectangle(0,0,1300,900,fill="white")
        self.canvas.create_text(650,75,text="Press the corresponding key for the right mode of game to play",fill="red",font="Arial  32  bold")
        self.canvas.create_text(650,225,text="In this game there are extra functionalities that have been added to make it more exciting",fill="red",anchor = "center", font="Helvetica 24 italic ")
        self.canvas.create_text(650,375,text="However if you choose to not play with these added functionalities, click below for your mode",fill="red",font="Helvetica 24 italic ")
        self.canvas.create_image(300,500, image = self.noFunctionsIMG)
        self.canvas.create_image(900, 500, image = self.functionsIMG)
        self.canvas.create_text(300, 650, text = "Enter 'o' to have no additional Functions(no draw 2, draw 4 or 7)", fill = "red", font = "Script 24 ")
        self.canvas.create_text(900, 650, text = "Enter 'O' to have all the additional functionalities",fill = "red", font = "Script 24")
        
    ###############################
    #Game Mode
    ###############################
    def gamemousePressed(self,event):

        if UserInterace.button(event.x,event.y):
                    print("yay")
                    self.sayUno = True
                    print(self.sayUno)
        if self.other == 0:
            if self.playerTurn == True:
                UnoGame.personPlay(self,event)
                print(self.moveMade, "I made this move")
                if self.moveMade == True:
                    if not self.reverse:
                        self.playerTurn = False
                        self.AIplayer1Turn = True
                    else:
                        self.playerTurn = False
                        self.AIplayer3Turn = True 
        elif self.other == 1:
            if self.playerTurn == True:
                UnoGame.personPlay(self,event)
                if self.moveMade == True:
                    if not self.reverse:
                        self.playerTurn = False
                        self.otherUser1 = True
                    else:
                        self.playerTurn = False
                        self.AIplayer3Turn = True
                self.next = True
            elif self.otherUser1 == True:
                UnoGame.personPlay(self,event)
                if self.moveMade == True:
                    if not self.reverse:
                        self.otherUser1 = False
                        self.AIplayer2Turn = True
                    else:
                        self.otherUser1 = False
                        self.playerTurn = True
                    self.next = True
	            
	                    

            
    def gamekeyPressed(self,event):
        if event.keysym == "r" and self.gameOver == True:
            UnoGame.init(self)

    def gameredrawAll(self):
        

        self.canvas.create_rectangle(0,0,1300,1300, fill = "red")
        for table in self.table:
            self.canvas.create_image(650,450, image = table)
        comp1face = self.AIplayer1
        self.canvas.create_image(650,60, image = comp1face)
        if self.other == 1:
            self.canvas.create_text(550, 60, text = "Friend", font = "Castellar 16 ", fill = "white")




















            
        else:self.canvas.create_text(550, 60, text = "Chidinma", font = "Castellar 16 ", fill = "white")
        comp2face = self.AIplayer2
        self.canvas.create_image(80,450, image = comp2face)
        self.canvas.create_text(80, 350, text = "Konama", font = "Castellar 16 ", fill = "white")
        comp3face = self.AIplayer3
        self.canvas.create_image(1210,450, image = comp2face)
        self.canvas.create_text(1210, 350, text = "Ubong", font = "Castellar 16 ", fill = "white")
        for card in self.deckFace:
            face = self.cards[Cards.getImage(card.kind,card.color)]
            unoBack = self.cards[-1]
            card.drawBackImage(self.canvas,face,unoBack)
        for card in self.playerHand:
            image = self.cards[Cards.getImage(card.kind,card.color)]
            card.drawUserHand(self.canvas,image)
        for card in self.top:
            image = self.cards[Cards.getImage(card.kind,card.color)]
            card.drawStartCard(self.canvas,image)

        for card in self.AI1:
            image = self.cards[Cards.getImage(card.kind,card.color)]
            unoBack = self.cards[-1]
            card.AI1Draw(self.canvas,unoBack)

        for card in self.AI2:
            image = self.cards[Cards.getImage(card.kind,card.color)]
            unoBack = self.cards[-1]
            card.AI2Draw(self.canvas,unoBack)

        for card in self.AI3:
            image = self.cards[Cards.getImage(card.kind,card.color)]
            unoBack = self.cards[-1]
            card.AI3Draw(self.canvas,unoBack)

        if self.level== "easy":
            for button in self.unoButton:
                self.canvas.create_image(700,500, image = button)
            
        else:
             for button in self.unoButton:
                self.canvas.create_image(700,475, image = button)
        if self.otherUser1 == True and self.timerDelay >= 10:
            self.canvas.create_text(650,650, text = "Friend's Turn!", font = "Arial 24 bold")

        if self.playerTurn == True:
            self.canvas.create_text(650,650, text = "Your Turn!", font = "Arial 24 bold")
        if self.AIplayer1Turn == True:
        	self.canvas.create_text(650,50, text = "Chidinma's Turn!", font = "Arial 24 bold")
        if self.AIplayer2Turn == True:
        	self.canvas.create_text(150,150, text = "Konama's Turn!", font = "Arial 24 bold")
        if self.AIplayer3Turn == True:
        	self.canvas.create_text(1000,150, text = "Ubong's Turn!", font = "Arial 24 bold")
        if self.reverse == True:
        	self.canvas.create_rectangle(0,0,100,100, fill = "purple")
        	self.canvas.create_text(50,50, text = "Reverse!", fill = "white", font = "Arial 14 bold")



        if self.gameOver:
            self.canvas.create_image(350,350,image=self.winningBackground)
            self.canvas.create_text(350,350, text=self.winner,font="Times 52 italic bold", fill = "white")#replace with self.winner
            self.canvas.create_text(750,350, text="WON!!!!!!!!!!!",font="Times 52 italic bold", fill = "white")
            self.canvas.create_image(350,450,image=self.winningFace)#replace with self.winnerFace
            
            self.canvas.create_text(650,575, text = "Press R To Play Again!", font="Times 34 italic bold",fill = "white")
            self.AIplayer1Turn= False
            self.AIplayer2Turn = False 
            self.AIplayer3Turn = False 
    def gametimerFired(self):
        #####################################
        # Multiplayer
        #####################################
        print(self.other)
        print(self.next)
        if self.other == 1 :
            self.timerDelay += 1
            if self.otherUser1 == True and self.timerDelay % 10 == 0 and self.next == True and self.gameOver == False:
                temp = self.playerHand
                self.playerHand = self.AI1
                self.AI1 = temp
                self.playerHand = Hand.reloadHand(self.playerHand)
                self.AI1 = AI1Hand.reloadHand(self.AI1)
                self.next = False
            elif self.playerTurn == True and self.timerDelay % 10 ==0 and self.next == True and self.gameOver == False:
                temp = self.playerHand
                self.playerHand = self.AI1
                self.AI1 = temp
                self.playerHand = Hand.reloadHand(self.playerHand)
                self.AI1 = AI1Hand.reloadHand(self.AI1)
                self.next = False
            

        
        #####################################
        #Options Check
        #####################################
        
           
        if self.other == 1:        
            if len(self.AI1) ==1:
                print("I have one card left")
                if self.sayUno == False and self.AIplayer2Turn == True:
                    for i in range(2):
                        card = random.choice(self.deck)
                        self.AI1.append(card)
                    self.playerHand = Hand.reloadHand(self.playerHand)
        if len(self.playerHand) ==1:
            print("I have one card left")
            if self.sayUno == False and self.AIplayer2Turn == True:
                for i in range(2):
                    card = random.choice(self.deck)
                    self.playerHand.append(card)
                self.playerHand = Hand.reloadHand(self.playerHand)
       

        if len(self.AI1) == 1:
            self.tomUNO = True

        elif len(self.AI2) == 1:
            self.richardUNO = True 

        elif len(self.AI3) == 1:
            self.harryUNO = True


        

        ########################################
        #Uno Check 
        #########################################
        if len(self.playerHand) == 0:
            self.winner = "YOU"
            self.winnerFace = self.winningFace
            self.gameOver = True
        if len(self.AI1) == 0 and self.other == 1 and self.playerTurn == True:
            self.winner = "Friend"
            self.gameOver = True

        if len(self.AI1) == 0:
            self.winnerFace = self.AIplayer1
            self.winner = "Chidinma"
            self.gameOver = True 

        if len(self.AI2) == 0:
            self.winnerFace = self.AIplayer2
            self.winner = "Konama"
            self.gameOver = True

        if len(self.AI3) == 0:
            self.winnerFace = self.AIplayer3
            self.winner = "Ubong"
            self.gameOver = True
#######################################################################
#Shuffle hand
#######################################################################
        if self.option != "noFunctions" and self.other == 0:
            self.pause += 1
            if self.top[-1].kind == 7 and self.switched == True and self.pause % 15 == 0:
        	    self.switched = False
            if self.top[-1].kind == 7 and self.switched == False:
        	    temp = self.playerHand
        	    self.playerHand = self.AI1
        	    self.AI1 = self.AI2
        	    self.AI2 = self.AI3
        	    self.AI3 = temp
        	    self.playerHand = Hand.reloadHand(self.playerHand)
        	    self.AI1 = AI1Hand.reloadHand(self.AI1)
        	    self.AI2 = AI2Hand.reloadHand(self.AI2)
        	    self.AI3 = AI3Hand.reloadHand(self.AI3)
        	    self.switched = True
#######################################################################  
# Reverse and Reload Deck
#######################################################################   	
        
        if len(self.deck) < 10:
        	self.deck = self.top[:-1]
        if self.top[-1].kind == 10 and self.reverse == False:
        	self.reverse = True
        elif self.top[-1].kind == 10 and self.reverse == True:
            self.reverse = False

        	
###########################################################################
#Draw 2 Function
###########################################################################
        
        if self.isPick2 == True:
            if self.playerTurn == True:
                for i in range (2):
                    card = random.choice(self.deck)
                    self.playerHand.append(card)
                self.playerHand = Hand.reloadHand(self.playerHand)
                self.playerTurn = False
                self.isPick2 = False
                if self.other == 1:
                    if not self.reverse:
                        self.otherUser1 = True
                    else:
                        self.AIplayer3Turn = True
                else:
                    if not self.reverse:
                        self.AIplayer1Turn = True
                    else:
                        self.AIplayer3Turn = True
            if self.otherUser1 ==True:
                for i in range (2):
                    card = random.choice(self.deck)
                    self.AI1.append(card)
                self.AI1 = AI1Hand.reloadHand(self.playerHand)
                self.otherUser1 = False
                self.isPick2 = False
                if self.other == 1:
                    if not self.reverse:
                        self.AIplayer2Turn= True
                    else:
                        self.playerTurn = True
                

            elif self.AIplayer1Turn == True:
                for i in range (2):
                    card = random.choice(self.deck)
                    self.AI1.append(card)
                self.AI1 = AI1Hand.reloadHand(self.AI1)
                self.isPick2 = False
                self.AIplayer1Turn = False
                if not self.reverse:
                    self.AIplayer2Turn = True
                else:
                    self.playerTurn = True
            elif self.AIplayer2Turn == True:
                for i in range (2):
                    card = random.choice(self.deck)
                    self.AI2.append(card)
                self.AI2 = AI2Hand.reloadHand(self.AI2)
                self.isPick2 = False
                self.AIplayer2Turn = False
                if self.other == 1:
                    if not self.reverse:
                        self.AIplayer3Turn = True
                    else:
                        self.otherUser1 = True
                else:
                    if not self.reverse:
                        self.AIplayer3Turn = True
                    else:
                        self.AIplayer1Turn = True
            elif self.AIplayer3Turn == True:
        	    for i in range (2):
        	    	card = random.choice(self.deck)
        	    	self.AI3.append(card)
        	    
        	    self.isPick2 = False
        	    self.AIplayer3Turn = False
        	    if not self.reverse:
        	        self.playerTurn = True
        	    else:
        	    	self.AIplayer2Turn = True
#############################################################################
# Draw 4
#############################################################################
         

        if self.isPick4 == True:
            if self.playerTurn == True:
       	        for i in range (4):
                    card = random.choice(self.deck)
                    self.playerHand.append(card)
                self.playerHand = Hand.reloadHand(self.playerHand)
                self.playerTurn = False
                self.isPick4 = False
                if self.other == 1:
                    if not self.reverse:
                        self.otherUser1 = True
                    else:
                        self.AIplayer3Turn = True
                else:
                    if not self.reverse:
                        self.AIplayer1Turn = True
                    else:
                        self.AIplayer3Turn = True
            elif self.otherUser1 == True:
                for i in range(4):
                    card = random.choice(self.deck)
                self.AI1 = AI1Hand.reloadHand(self.AI1)
                print(self.AI1)

                self.otherUser1 = False
                self.isPick4 = False
                if not self.reverse:
                    self.AIplayer2Turn = True
                else:
                    self.playerTurn = True

            elif self.AIplayer1Turn == True:
       	        for i in range (4):
                    card = random.choice(self.deck)
                    self.AI1.append(card)
                self.AI1 = AI1Hand.reloadHand(self.AI1)
                self.isPick4 = False
                self.AIplayer1Turn = False
                if not self.reverse:
                    self.AIplayer2Turn = True
                else:
                    self.playerTurn = True
            elif self.AIplayer2Turn == True:
       	        for i in range (4):
                    card = random.choice(self.deck)
                    self.AI2.append(card)
                self.AI2 = AI2Hand.reloadHand(self.AI2)
                self.isPick4 = False 
                self.AIplayer2Turn = False
                if self.other == 1:
                    if not self.reverse:
                        self.AIplayer3Turn = True
                    else:
                        self.otherUser1 = True
                else:
                    if not self.reverse:
                        self.AIplayer3Turn = True
                    else:
                        self.AIplayer1Turn = True
            elif self.AIplayer3Turn == True:
       	        for i in range (4):
                    card = random.choice(self.deck)
                    self.AI3.append(card)
                
                self.isPick4 = False
                self.AIplayer3Turn = False
                if not self.reverse:
                    self.playerTurn = True
                else:
                    self.AIplayer2Turn = True
#############################################################################
#Skip Function 
#############################################################################
        
        if self.isSkip == True:
            if self.playerTurn == True:
                self.playerTurn = False
                self.isSkip = False
                if self.other == 1:
                    if not self.reverse:
                        self.otherUser1 = True
                    else:
                        self.AIplayer3Turn = True
                elif self.other == 0:
                    if not self.reverse:
                        self.AIplayer1Turn = True
                    else:
                        self.AIplayer3Turn = True
            elif self.otherUser1 == True:
                self.otherUser1 = False
                self.isSkip = False
                self.next = False
                if not self.reverse:self.AIplayer2Turn = True
                else: self.playerTurn = True
            elif self.AIplayer1Turn == True:
        	    self.AIplayer1Turn = False
        	    self.isSkip = False
        	    if not self.reverse:
        	        self.AIplayer2Turn = True
        	    else:
        	    	self.playerTurn = True
            elif self.AIplayer2Turn == True:
                self.AIplayer2Turn = False
                self.isSkip = False 
                if self.other == 1:
        	        if not self.reverse:
        	           self.AIplayer3Turn = True
        	        else:
                	  self.otherUser1 = True
                else:
                    if not self.reverse:
                       self.AIplayer3Turn = True
                    else:
                      self.AIplayer1Turn = True
            elif self.AIplayer3Turn == True:
        	    self.AIplayer3Turn = False
        	    self.isSkip = False 
        	    if not self.reverse:
        	        self.playerTurn = True
        	    else:
        	    	self.AIplayer2Turn = True





   



            
        	    
       
        


###########################################################################
# AI Player 1
###########################################################################
        if self.AIplayer1Turn == True:
        
            self.timerDelay += 1
            

            if self.timerDelay % 5 == 0 and self.timerDelay != 0:
                print("yay")
                
                self.legal = AI1Hand.legalCardExists(self.top, self.AI1)

                if self.legal == True:
                    if self.level == "easy":
                        self.test = AI1Hand.AI1EasyMove(self, self.AI1,self.top)
                    else:
                        self.test = AI1Hand.AI1HardMove(self,self.AI1,self.top)
                    
                    if self.test == None:
                    	self.legal = False
                
                    a = self.AI1.index(self.test)

                    self.going = self.AI1.pop(a)
                    

                if Cards.checkIsLegal(self.going,self.top):
                        self.back=self.top[0]
                        Cards.changePos(self.going,self.back)
                        self.top.append(self.going)#if the card is in the hand change its x and y back to the original
                        self.isSkip = Cards.checkSkip(self.top)
                        self.isPick2 = Cards.checkDraw2(self.top)
                        self.isPick4 = Cards.checkDraw4(self.top)
                        self.AI1 = AI1Hand.reloadHand(self.AI1)
                        if self.going.kind == 14:
                        	self.AIplayer1Turn = True 
                        else:
                            self.moveMade=True
                            if not self.reverse:
                                self.AIplayer1Turn = False
                                self.AIplayer2Turn = True 
                            else:
                                self.AIplayer1Turn = False
                                self.playerTurn = True
                    
                elif not self.legal:
                    if self.picked == False:
                        self.removed = AI1Hand.pickCards(self)
                        self.pickedUp = True
                        self.moveMade = True 
                        if not self.reverse:
                            self.AIplayer1Turn = False
                            self.AIplayer2Turn = True 
                        else:
                            self.AIplayer1Turn = False
                            self.playerTurn = True
                        self.timerDelay = 0


######################################################################
#AI Player 2
#######################################################################
       
        if self.AIplayer2Turn == True:
            
       	    self.timerDelay += 1
           
            if self.timerDelay % 5 == 0 and self.timerDelay != 0:
                print("I got this far")
                self.legal = AI2Hand.legalCardExists(self.top, self.AI2)

                if self.legal == True:
                  
                    if self.level == "easy":
                        self.test = AI2Hand.AI2EasyMove(self,self.AI2,self.top)
                    else:
                        self.test = AI2Hand.AI2HardMove(self,self.AI2,self.top)
                    if self.test == None:
                    	self.legal = False
                    print(self.test)
                    a = self.AI2.index(self.test)

                    self.going = self.AI2.pop(a)
                    if not Cards.checkIsLegal(self.going,self.top):
                        self.AI2.append(self.going)
                    print(self.going)
                    self.back=self.top[0]
                    Cards.changePos(self.going,self.back)
                    self.top.append(self.going)#if the card is in the hand change its x and y back to the original
                    self.isSkip = Cards.checkSkip(self.top)
                    self.isPick2 = Cards.checkDraw2(self.top)
                    self.isPick4 = Cards.checkDraw4(self.top)
                    self.AI2 = AI2Hand.reloadHand(self.AI2)
                    if self.going.kind == 13:
                    	self.AIplayer2Turn = True
                    self.moveMade=True
                    if self.other == 1:
                        if not self.reverse:
                            self.AIplayer2Turn = False 
                            self.AIplayer3Turn = True 
                        else:
                            self.AIplayer2Turn = False
                            self.otherUser1 = True
                    else:
                        if not self.reverse:
                            self.AIplayer2Turn = False 
                            self.AIplayer3Turn = True 
                        else:
                            self.AIplayer2Turn = False
                            self.AIplayer1Turn = True

                    self.timerDelay = 0
                elif not self.legal:
                    if self.picked == False:
                        self.removed= AI2Hand.pickCards(self)
                        self.pickedUp = True
                        self.moveMade = True
                        if self.other == 1:
                            if not self.reverse:
                                self.AIplayer2Turn = False 
                                self.AIplayer3Turn = True 
                            else:
                                self.AIplayer2Turn = False
                                self.otherUser1 = True
                        else:
                            if not self.reverse:
                                self.AIplayer2Turn = False 
                                self.AIplayer3Turn = True 
                            else:
                                self.AIplayer2Turn = False
                                self.AIplayer1Turn = True 
                        self.timerDelay = 0  

########################################################################
# AI Player 3
#######################################################################
        
        if self.AIplayer3Turn == True:
            self.timerDelay += 1

            if self.timerDelay% 5 == 0 and self.timerDelay != 0:
                self.legal = AI3Hand.legalCardExists(self.top, self.AI3)
                print("let's check this out")

                if self.legal == True:
                    if self.level == "easy":
                        print(self.AI3)
                        self.test = AI3Hand.AI3EasyMove(self,self.AI3,self.top)
                    else:
                        self.test = AI3Hand.AI3HardMove(self,self.AI3,self.top)
                    if self.test == None:
                    	self.legal = False
                    a = self.AI3.index(self.test)

                    self.going = self.AI3.pop(a)
                    print(self.going)
                    if not Cards.checkIsLegal(self.going,self.top):
                        self.AI3.append(self.going)
                  
                    self.back=self.top[0]
                    Cards.changePos(self.going,self.back)
                    self.top.append(self.going)#if the card is in the hand change its x and y back to the original
                    self.AI3 = AI3Hand.reloadHand(self.AI3)
                    self.isSkip = Cards.checkSkip(self.top)
                    self.isPick2 = Cards.checkDraw2(self.top)
                    self.isPick4 = Cards.checkDraw4(self.top)
                    self.moveMade=True
                    if self.going.kind == 13:
                    	self.AIplayer3Turn = True
                    elif not self.reverse:  
                        self.AIplayer3Turn = False 
                        self.playerTurn = True
                    else:
                        self.AIplayer3Turn = False 
                        self.AIplayer2Turn = True
                    self.timerDelay = 0 
                    
                elif not self.legal:
                    if self.picked == False:
                        self.removed = AI3Hand.pickCards(self)
                        self.pickedUp = True
                        self.moveMade = True
                        if not self.reverse:  
                            self.AIplayer3Turn = False 
                            self.playerTurn = True
                        else:
                            self.AIplayer3Turn = False 
                            self.AIplayer2Turn = True
                        self.timerDelay = 0


           
#######################################################################################################################################
#Check wild Cards and Functions 
#######################################################################################################################################
        
    def personPlay(self,event):
        if self.picked == True:
            self.picked = False
        for card in self.deck:
            if card.deckContains(event.x,event.y) and self.picked == False: 
                self.removed = Hand.pickCards(self)
                self.picked = True 
                self.moveMade = True
                
        for card in self.playerHand:

            if card.handContains(event.x,event.y, card.x, card.y):

                self.test = card
                
                self.mistakeCount=0     
                # or self.top[0].kind=="Wild Draw +4" or self.top[0].kind=="Wild Card":
                a=self.playerHand.index(card)
                
                    
                self.going=self.playerHand.pop(a)
                
              
                    
                if Cards.checkIsLegal(self.going,self.top):

                    self.back=self.top[0]
                    Cards.changePos(self.going,self.back)
                    self.top.append(self.going)#if the card is in the hand change its x and y back to the original
                    self.isSkip = Cards.checkSkip(self.top)
                    self.isPick2 = Cards.checkDraw2(self.top)
                    self.isPick4 = Cards.checkDraw4(self.top)
                    self.playerHand = Hand.reloadHand(self.playerHand)
                    self.moveMade=True


                else:
                    self.playerHand.append(self.going) 
                           




class Cards(object):
    colors = ['black','green', 'blue','red', 'yellow']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7","8", "9", "reverse", "stop", "+2", "wildcard", "+4"]
    width = 1300
    height = 1300
    
    def __init__(self,x,y,kind,color="black"):

        self.x=x
        self.y=y
        self.wide=50
        self.length=75
        self.kind=kind
        self.color=color
        
        self.d=(((self.wide**2)+(self.length**2))**.05)

    def __repr__(self):
        return (" A %s %s" %
                (Cards.colors[self.color],Cards.numbers[self.kind]))

    def getHashables(self):
        return (self.kind, self.color) # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, Cards) and
                (self.kind == other.kind) and
                (self.color == other.color))
    
    

    ###################################
    #Wild Card Functions
    ####################################

    def reverse(order):
        newOrder = copy.deepcopy(order)
        newOrder = order[::-1]
        return newOrder

    def changeOrder(L):
        order=copy.deepcopy(L)
        back=order.pop(0)
        order.append(back)
        return order

    
    def checkIsLegal(card,top):
        print(top[0])
        if top[-1] == None:
    	    return True 
        elif card.kind == top[-1].kind or card.color == top[-1].color:
            return True
        elif card.kind ==  13 or card.kind == 14:
        	return True
        elif top[-1].kind == 13 or top[-1].kind == 14:
        	return True
        else:
        	return False
    def checkSkip(top):
    	if top[-1].kind == 11 and top[-1].kind != None:
    		return True 
    def checkDraw2(top):
    	if top[-1].kind == 12 and top[-1].kind  != None:
    		return True 
    def checkDraw4(top):
    	if top[-1].kind == 14 and top[-1].kind != None:
    		return True

    def changePos(going,back):
        going.x = back.x

    def changeYPos(going,back):
        going.y = back.y

    def changeDeckPos(back): # double check
        back.x = 650    


    def deckContains(self, x, y):
        return (450 <= x <= 550 and 375 <= y <= 575 )
        

    def handContains(self, x, y, x1, y1):
        
        
        return (x1-50<= x <= x1 + 250 and y1 - 100 <= y <= y1 + 100)

    

    #creatin users hand of cards
    ######################################################################
    #getting cards both image and deck     

    def loadImage():
        totalCards = 52
        i = 0
        #representing the four main colors
        color=["g","b","r","y"]
        images = []
        for card in range(totalCards):
            if card % 13 == 0 and card != 0:
                i += 1
            number = (card%13)
            filename = "cards/%s%d.png"%(color[i],number)
            image = Image.open(filename)
            image = image.resize((100, 200), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            images.append(image)
        names = ['+4', 'wildcard']
        i = 0 
        for card in range(2):
            filename = "cards/%s.png"%(names[i])
            image = Image.open(filename)
            image = image.resize((100, 200), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            images.append(image)
            i += 1
        backcardFile = "cards/backcard.png"
        backcard = Image.open(backcardFile)
        backcard = backcard.resize((100,200), Image.ANTIALIAS)
        backcard = ImageTk.PhotoImage(backcard)
        images.append(backcard)
        return images

    def getImage(kind,color):
        if kind == 13 and color == 0:
            return 53
        if kind == 14 and color == 0:
            return 52
        else:
            index = ((color-1)*13)+kind
            
            return index
    def drawLights(self,canvas,image):
    	canvas.create_image(650, 100, image = image)

    def drawBackImage(self,canvas,image,back):
        

        canvas.create_image(500,475,image=image)
        canvas.create_image(500,475,image=back)
    def drawUserHand(self,canvas,image):
        Userx = self.x
        UserY = self.y - 50
        canvas.create_image(Userx+200,UserY+55,image=image)
    def drawStartCard(self,canvas,image):
        canvas.create_image(850,450,image=image)
    def AI1Draw(self,canvas,image):
        Hx=self.x
        # Hy=100
        Hy=self.y-350
        canvas.create_image(Hx+50,Hy-10,image=image)

    def AI2Draw(self,canvas,image):
        Hx=self.x-470
        # Hy=100
        Hy=self.y-90
        canvas.create_image(Hx+50,Hy+75,image=image)

    def AI3Draw(self,canvas,image = "cards/wildcard.png"):
        Hx = self.x + 370
        # Hy=100
        Hy = self.y - 90
        canvas.create_image(Hx+50,Hy+75,image=image)

class UnoDeck(Cards):
    

    def loadDeck(shuffled = True):
        deck = []
        for times in range(2):
            for number in range(1,len(Cards.numbers)-2):
                for color in range(1,5):
                    deck.append(Cards(Cards.width//2,Cards.height//2,number,color))
        

        for special in range(4):
            deck.append(Cards(Cards.width//2,Cards.height//2,13,0))
            deck.append(Cards(Cards.width//2,Cards.height//2,14,0))

        for color in range(1,len(Cards.colors)):
            deck.append(Cards(Cards.width//2,Cards.height//2,0,color))

        if (shuffled):
            random.shuffle(deck)
        return deck
    deck = loadDeck()

class Hand(Cards):

    def __init__(self,x,y,kind,color="black"):
        super().init(x,y,kind,color="black")
        
    
    def loadHand(deck):
        completeDeck = copy.deepcopy(deck)
        hand = []
        change = 150
        for cards in range(7):
            n = random.randint(1,len(completeDeck) - 1)
            card = completeDeck.pop(n)
            card.x = change
            card.y = 650 
            hand.append(card)
            change += 100
        
        return hand 

    def reloadHand(hand):
        change = 150
        newHand = []
        for card in hand:

    	    card.x = change 
    	    card.y = 650
    	    newHand.append(card)
    	    change += 100
        return newHand
                 
    def legalCardExists(hand,top):
        for card in hand:
            if Cards.checkIsLegal(card,top):
                return True 
        return False 

    

   
        

    def pickCards(self):
        for cards in range(1):
            n = random.randint(0,len(self.deck)-1)
            card = self.deck.pop(n)
            self.playerHand.append(card)
        self.playerHand = Hand.reloadHand(self.playerHand)
        return card


class AI1Hand(Cards):
    def __init__(self,x,y,kind,color="black"):
        super().init(x,y,kind,color="black")
        

    def loadHand(deck):
        completeDeck = copy.deepcopy(deck)
        hand = []
        change = 450
        for cards in range(7):
            n = random.randint(1,len(completeDeck) - 1)
            card = completeDeck.pop(n)
            card.x = change
            card.y = 550
            
            hand.append(card)
            change += 50
        

        return hand 

    def reloadHand(hand):
        change = 450
        newHand = []
        for card in hand:

    	    card.x = change 
    	    card.y = 550
    	    newHand.append(card)
    	    change += 50
        return newHand
   

    def pickCards(self):
        for cards in range(1):
            n = random.randint(0,len(self.deck)-1)
            card = self.deck.pop(n)
            self.AI1.append(card)
        return card
    def legalCardExists(hand,top):
        for card in hand:
            if Cards.checkIsLegal(card,top):
                return True 
        return False 

    def AI1EasyMove(self,hand, top):
         
        best = 14 
        bestCard = None
         
        for card in hand:
            if Cards.checkIsLegal(card,top):
                
                if card.kind <= best:
                    best = card.kind
                    bestCard = card
        if bestCard == None:
        	bestCard = AI1Hand.pickCards(self) 
        print(bestCard)
        return bestCard 

        
    def AI1HardMove(self, hand,top):
        best = 0 
        bestCard = None
         
        for card in hand:
            if Cards.checkIsLegal(card,top):
                if card.kind >= best or card.kind == 7:
                    best = card.kind
                    bestCard = card
                if card.kind == 7 and len(self.playerHand) < 3:
                	bestCard = card
        if bestCard == None:
        	bestCard = AI1Hand.pickCards(self) 

        print(bestCard)
        return bestCard 


class AI2Hand(Cards):
    def __init__(self,x,y,kind,color="black"):
        super().init(x,y,kind,color="black")

    def loadHand(deck):
        completeDeck = copy.deepcopy(deck)
        hand = []
        change = 300
        for cards in range(7):
            n = random.randint(1,len(completeDeck) - 1)
            card = completeDeck.pop(n)
            card.y = change 
            hand.append(card)
            change += 50
        
        return hand 
    
    def reloadHand(hand):
        change = 300
        newHand = []
        for card in hand: 
    	    card.y = change
    	    newHand.append(card)
    	    change += 50
        return newHand

 

    def pickCards(self):
        for cards in range(1):
            n = random.randint(0,len(self.deck)-1)
            card = self.deck.pop(n)
            self.AI2.append(card)
        return card

    def legalCardExists(hand,top):
        for card in hand:
            if Cards.checkIsLegal(card,top):
                return True 
        return False 

    def AI2EasyMove(self,hand, top):
        best = 14 
        bestCard = None
         
        for card in hand:
            if Cards.checkIsLegal(card,top):
                
                if card.kind <= best:
                    best = card.kind
                    bestCard = card
        if bestCard == None:
        	bestCard = AI2Hand.pickCards(self) 
        print(bestCard)
        return bestCard
    
    def AI2HardMove(self,hand,top):
        best = 0 
        bestCard = None
         
        for card in hand:
            if Cards.checkIsLegal(card,top):
                
                if card.kind >= best:
                    best = card.kind
                    bestCard = card
        if bestCard == None:
        	bestCard = AI2Hand.pickCards(self) 
        print(bestCard)
        return bestCard 

class AI3Hand(Cards):
    def __init__(self,x,y,kind,color="black"):
        super().init(x,y,kind,color="black")

    def loadHand(deck):
        completeDeck = copy.deepcopy(deck)
        hand = []
        change = 300
        for cards in range(7):
            n = random.randint(1,len(completeDeck) - 1)
            card = completeDeck.pop(n)
            card.y = change 
            hand.append(card)
            change += 50
        
        return hand 

    def reloadHand(hand):
        change = 300
        newHand = []
        for card in hand: 
            card.x = 675
            card.y = change
            newHand.append(card)
            change += 50
        return newHand

    def pickCards(self):
        for cards in range(1):
            n = random.randint(0,len(self.deck)-1)
            card = self.deck.pop(n)
            self.AI3.append(card)
        return card

    def legalCardExists(hand,top):
        for card in hand:
            if Cards.checkIsLegal(card,top):
                return True 
        return False 

    def AI3EasyMove(self,hand, top):
        best = 14 
        bestCard = None 
        for card in hand:
            if Cards.checkIsLegal(card,top): 
                if card.kind <= best:
                    best = card.kind
                    bestCard = card 
        if bestCard == None:
        	bestCard = AI3Hand.pickCards(self)
        return bestCard
        
    def AI3HardMove(self,hand,top):
        best = 0 
        bestCard = None
         
        for card in hand:
            if Cards.checkIsLegal(card,top):
                
                if card.kind >= best:
                    best = card.kind
                    bestCard = card
        if bestCard == None:
        	bestCard = AI1Hand.pickCards(self) 
        print(bestCard)
        return bestCard 
####################################################################################################################
#GUI
###################################################################################################################
#All Images loaded here were gotten from google
class UserInterace(object):
    def __init__(self):
        pass
    def loadWars():
        filename = "unogame.png"
        image = ImageTk.PhotoImage(Image.open(filename))
        return [image] 
    def loadWinningBackground():
        filename = "winningBackground.jpg"
        image = Image.open(filename)
        image = image.resize((2000, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def loadWinner():
        filename = "winningFace.png"
        image = Image.open(filename)
        image = image.resize((100, 100), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def loadPlayers():
        players = []
        for i in range(1,4):
            filename = "player.png"
            image = Image.open(filename)
            image = image.resize((100, 100), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            players.append(image)
        return players

    def loadTable():
        filename = "table.png"
        image = Image.open(filename)
        image = image.resize((900, 650), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def loadBackground():
        filename = "uno.jpg"
        image = Image.open(filename)
        image = image.resize((600, 600), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]
    def loadGIF():
    	filename = "background.gif"
    	image = ImageTk.PhotoImage(Image.open(filename))
    	return [image]


    def loadnoFunctionImage():
        filename = "noFunctions.jpg"
        image = Image.open(filename)
        image = image.resize((150, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def loadFunctionsImage():
        filename = "functions.jpg"
        image = Image.open(filename)
        image = image.resize((150, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def loadUnoButton():
        filename = "unoButton.png"
        image = Image.open(filename)
        image = image.resize((75, 75), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        return [image]

    def button(x,y):
        print(x - 35 <= 700 <= x + 35 and y - 35 <= 500 <= y +35)
        return (x - 35 <= 700 <= x + 35 and y - 35 <= 500 <= y +35)



game= UnoGame()
game.run(1300,1300)
