
import sys, pygame,time,easygui,random
clock = pygame.time.Clock()
startover=""                              #when the game starts the buttons in the game loop disables in the beginning are:
                                                                                                    #bet button, betting text, choose winner, the cards button to pick up and etc.

betbutton=False
leavebutton=True
betting=False
pickbutton=False
shufflebutton=True
aistart=False
show1=False
show=False
gamer=False
start=""
cards = ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]
cards1= ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]
humancard=""
aicard=""                       # list of cards in a deck
ainumber=""
humannumber=""
tiechose=""

pygame.init()  # starting pygame

coins=1000     #1000 coins alloted



amnt=0
pygame.init()        #amount bet set to 0 for now

size = width, height = 1350, 750        #pixels of the game screen

black = 0,0,0
blue= 63,72,204
white=255,255,255
orange=255,69,0
gold=255,215,0              #colors
red= 255,0,0


screen = pygame.display.set_mode((size))

def intro():
    global coins
    global orange
    global black
    global blue

    logo = pygame.image.load("logo.png")
    dealer= pygame.image.load("dealer.png")
    while 1:                                        #starting the gamer
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:              #force exit not recommended
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


        screen.fill(orange) #screen color



        screen.blit(logo,(0,0))                             #game graphics
        button(100,600,250,100,gold,red,leave)                          # leave button
        myfont = pygame.font.Font(None,100)    #create text on button
        mytext = myfont.render("Quit",True,blue)
        screen.blit(mytext,(130,625))


        button(1050,600,250,100,gold,red,rules) #press next to go to the next screen
        myfont = pygame.font.Font(None,100)    #create text on button
        mytext = myfont.render("Next",True,blue)
        screen.blit(mytext,(1100,625))


        myfont = pygame.font.Font(None,50)    #create text on button
        mytext = myfont.render("Coins: {0}".format(coins),True,blue) #number of coins user has
        screen.blit(mytext,(1150,2))



        pygame.display.flip()
        clock.tick(60)
    pygame.quit

def leave():
    pygame.quit()
    sys.exit()           #when leave is pressed in a game
def rules():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.QUIT: #rules screen
                pygame.quit()
                sys.exit()                 # force exit, not recommended
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        screen.fill(black)


        rules = pygame.image.load("rules.png")  #getting the rules picture
        screen.blit(rules,(0,0))
        button(100,600,250,100,gold,red,leave)  #leave button
        myfont = pygame.font.Font(None,100)    #create text on button
        mytext = myfont.render("Quit",True,blue)
        screen.blit(mytext,(130,625))


        button(1050,600,250,100,gold,red,gameloop) #start butoon
        myfont = pygame.font.Font(None,100)    #create text on button
        mytext = myfont.render("Start",True,blue)
        screen.blit(mytext,(1100,625))


        pygame.display.flip()
        clock.tick(60)
    pygame.quit


def button(x,y,w,h,ic,ac,action=None):
    global orange                            #function for the button
    global black
    global screen
    mouse = pygame.mouse.get_pos()   #mouse=position of cursor
    click = pygame.mouse.get_pressed()  #click position when right clicked

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))     #when the cursor is on rectangle then rectangle's color will change

        if click[0] == 1 and action != None:
            action()                                #when there is a click then the action occurs
            #create buttons based on parameters
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))  #have the button stay as it is
def gameloop():
    global cards
    global cards1
    global aiprogram
    cards = ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]
    cards1= ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]
    #new set of cards will be initialized when the game loops
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()                     #force shutdown by escape key and on X
        elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        screen.fill(blue)  #screen fill will be color blue


        game = pygame.image.load("game.png")
        screen.blit(game,(50,10))     #loads the game table

        back = pygame.image.load("backcard.png")  #back of card is uploaded
        screen.blit(back,(641,165))





        leavebuttongame()  #the leave button is intitalized
        shufflebuttongame() #the shuffle button is intitalized
        bettext()       #text to show bet amount is initalized
        betbuttongame() #the bet button is intitalized
        pickbuttongame() #the pick a card button is intitalized
        display()   #the card is displayed button is intitalized
        aimagic()  #the ai will play its turn
        display1()  #the card picked by ai will be displayed


        winner() #winner is shown




        myfont = pygame.font.Font(None,50)    #create text on button
        mytext = myfont.render("Coins: {0}".format(coins),True,white)
        screen.blit(mytext,(1150,2)) #the text for the amount of coin is displayed


        pygame.display.flip()
        clock.tick(60)
    pygame.quit


def shufflebuttongame():
    if shufflebutton==True: #when the shuffle button is enabled then the button will only intilized
        button(640,285,95,30,gold,red,shuffle)
        myfont = pygame.font.Font(None,37)         #create text on button
        mytext = myfont.render("Shuffle",True,blue)
        screen.blit(mytext,(640,285))

def shuffle():
    global shufflebutton
    global betbutton
    global leavebutton
    global cards
    global coins

    easygui.msgbox("Cards are now being shuffled please wait!") #when the cards wil shuffle
    start=easygui.buttonbox("The betting round is about to start!. When this round starts, you won't be able to quit the game until the bet is over, do you want to continue?",choices=("Yes","No"))
    #ask the user if he wants to continue
    if start=="Yes":
        show=False
        show1=False
        betbutton=True
        shufflebutton=False
        leavebutton=False       #the button to bet money is enabled, everyother button is disabled
        random.shuffle(cards) #the cards will be shuffled
def leavebuttongame():
    if leavebutton==True: #when leave button is enabled when it will display
        button(100,600,250,100,gold,red,leave) #leave button
        myfont = pygame.font.Font(None,100)    #create text on button
        mytext = myfont.render("Quit",True,blue)
        screen.blit(mytext,(130,625))

def betbuttongame():
    if betbutton==True: #if the bet money button is enabled then:
        button(640,285,95,30,gold,red,bet)      #leave button
        myfont = pygame.font.Font(None,36)         #create text on button
        mytext = myfont.render("Bet Now",True,blue)
        screen.blit(mytext,(640,285))

def bet():
    global amnt
    global betbutton
    global betting      #ask how much to bet
    amnt=easygui.integerbox("Please enter in the amount of coins you want to bet. The dealer will bet the same amount. Make sure you between between 1 to {0} coins".format(coins),"Betting Round",lowerbound=0,upperbound=coins)
    betbutton=False #disbale button to bet again
    betting=True

def bettext():
    global amnt
    global pickbutton
    if betting == True:  #when the bet text is enabled then the text to show the amount to bet will start
        myfont = pygame.font.Font(None,35)         #create text on button
        mytext = myfont.render("Betting Amount: {0} coins".format(amnt),True,white)
        screen.blit(mytext,(540,285))
        coinpic= pygame.image.load("Coins.png")
        screen.blit(coinpic,(650,315))
        pickbutton=True #button to pick up card is enabled
    else:
        pickbutton=False #if not then it remains disbaled




def pickbuttongame():
    if pickbutton==True:
        button(623,585,165,90,gold,red,pick) #button to pick a card up is enabled
        myfont = pygame.font.Font(None,42)         #create text on button
        mytext = myfont.render("Pick A Card",True,blue) #pick a card up will display
        screen.blit(mytext,(623,622))
def pick():
    global cards
    global cards1
    global humancard
    global humannumber
    global show
    global pickbutton
    global aistart
    humancard = cards[0]  # top card will be picked from the shuffled pile
    humannumber=cards1.index(humancard) #the card will be located on the unshuffled pile
    print humannumber #number of ranking for the card picked
    cards.remove(humancard) #card to be removed from the pile
    pickbutton=False #button to pick again will be disbaled

    show=True #boolean to show the card picked will be displayed
    aistart=True #the ai's turn will start

def display():
    global humancard
    global humancardload
    global show
    global aistart
    if show==True:
        humancardload = pygame.image.load("{0}.jpg".format(humancard))
        screen.blit(humancardload,(650,440))  #if told to show the card the card will be shown
    pickbutton=False


def aimagic():
    global show1
    global cards
    global cards1
    global aicard
    global ainumber
    global aistart
    global gamer
    if aistart==True:
        aicard = cards[0] #ai's turn, pick the top card from the shuffled pile

        easygui.msgbox("You choose your card, now let me chose mine!") #command to let ai choose
        ainumber=cards1.index(aicard) #find the card value on ranking


        print ainumber #print the card ranking
        cards.remove(aicard) #remove picked card from the pile
        aistart=False #ai turn will be disabled
        show1=True #card will be shown
        gamer=True # command to choose winner or tie


def display1():
    global aicard
    global aicardload
    global show1
    if show1==True:
        aicardload = pygame.image.load("{0}.jpg".format(aicard)) #show the card
        screen.blit(aicardload,(641,165))

def winner():
    pickbutton=False
    tiechose=""
    global humannumber
    global ainumber
    global gamer
    global tiechose
    global amnt
    global coins
    global betting
    global show
    global show1
    global shufflebutton
    global leavebutton
    global pickbutton
    global cards1
    global cards
    if gamer==True:   #choosing winner will be allowed




        if (humannumber==0 or humannumber==1 or humannumber==2 or humannumber==3) and (ainumber==0 or ainumber==1 or ainumber==2 or ainumber==3):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==4 or humannumber==5 or humannumber==6 or humannumber==7) and (ainumber==4 or ainumber==5 or ainumber==6 or ainumber==7):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==8 or humannumber==9 or humannumber==10 or humannumber==11) and (ainumber==8 or ainumber==9 or ainumber==10 or ainumber==11):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==12 or humannumber==13 or humannumber==14 or humannumber==15) and (ainumber==12 or ainumber==13 or ainumber==14 or ainumber==15):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==16 or humannumber==17 or humannumber==18 or humannumber==19) and (ainumber==16 or ainumber==17 or ainumber==18 or ainumber==19):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==20 or humannumber==21 or humannumber==22 or humannumber==23) and (ainumber==20 or ainumber==21 or ainumber==22 or ainumber==23):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==24 or humannumber==25 or humannumber==26 or humannumber==27) and (ainumber==24 or ainumber==25 or ainumber==26 or ainumber==27):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==28 or humannumber==29 or humannumber==30 or humannumber==31) and (ainumber==28 or ainumber==29 or ainumber==30 or ainumber==31):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==32 or humannumber==33 or humannumber==34 or humannumber==35) and (ainumber==32 or ainumber==33 or ainumber==34 or ainumber==35):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==36 or humannumber==37 or humannumber==38 or humannumber==39) and (ainumber==36 or ainumber==37 or ainumber==38 or ainumber==39):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==40 or humannumber==41 or humannumber==42 or humannumber==43) and (ainumber==40 or ainumber==41 or ainumber==42 or ainumber==43):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter
        elif (humannumber==44 or humannumber==45 or humannumber==46 or humannumber==47) and (ainumber==44 or ainumber==45 or ainumber==46 or ainumber==47):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter

        elif (humannumber==48 or humannumber==49 or humannumber==50 or humannumber==51) and (ainumber==48 or ainumber==49 or ainumber==50 or ainumber==51):
            tiechose=easygui.buttonbox("This game is a tie! Do you want to surrender or go to war?", "Tie", choices=["Surrender", "Go to war"])
            tiebreak1()
            #when computer and human chooses same card number or letter

        elif humannumber>ainumber:
            easygui.msgbox("You won the bet, your card was higher in ranking!") #declare winner
            coins+=amnt#bet will be added to coins
            #when human is the winner

            gamebreak()#play again command
        elif humannumber<ainumber:
            easygui.msgbox("You lost the bet!") #declare loser
            coins-=amnt#lose bet

            gamebreak() #play again command



def gamebreak():
    global startover
    global cards
    global cards1
    global shufflebutton
    global leavebutton
    global gamer
    global betting
    global coins
    if coins==0:
        easygui.msgbox("You don't have any coins!") #if coins run out
        gamer=False  #every button except to quit will be disabled
        betting=False
        leavebutton=True
        # commands to play again
    else:
        startover=easygui.buttonbox("Do you want to bet again?", "Leave or Play", choices=["Yes", "No"])
        #ask to play again or no
        if startover=="Yes": #when play again
            cards = ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]
            cards1= ["2C","2S","2D","2H","3C","3S","3D","3H","4C","4S","4D","4H","5C","5S","5D","5H","6C","6S","6D","6H","7C","7S","7D","7H","8C","8S","8D","8H","9C","9S","9D","9H","10C","10S","10D","10H","JC","JS","JD","JH","QC","QS","QD","QH","KC","KS","KD","KH","AC","AS","AD","AH"]

            shufflebutton=True
            leavebutton=True
            gamer=False
            betting=False  #starts loop again, shuffle button and leavebutton will be on
        if startover=="No":
            leavebutton=True # asked to leave again
            betting=False
            gamer=False
def tiebreak1():
    global tiechose
    global coins
    global gamer
    global betting
    global leavebutton
    global pickbutton
    global amnt
    global cards
    if tiechose=="Surrender":
        easygui.msgbox("You will take away half of your bet!")
        coins-=amnt/2 #half the bet will be detucted again
        gamer=False
        betting=False
        leavebutton=True #ask to leave
    if tiechose=="Go to war":
        amnt=amnt*2 #bet to be increased y x2
        easygui.msgbox("Your bet will be doubled now!")
        pickbutton=True #told to pick again
        gamer=False







#------------------------------------------------------------------------maincode-----------------------------------------------------------
intro()