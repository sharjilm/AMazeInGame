import mainMenu
import pygame
import pauseButton
import exitButton

class MenuController():
    def __init__(self):
        self.mm = mainMenu.MainMenu()
        self.gameStarted = False
        self.inSettings = False
        self.paused = False

    def createButtons(self):
        self.pb = pauseButton.PauseButton()
        self.eb = exitButton.ExitButton()
        self.pb.setMC(self)
        self.eb.setMC(self)

    def checkButtons(self):
        self.pb.read()
        self.eb.read()

    def displayButtons(self):
        self.mm.displayButtons()

    def update(self):
        if not self.gameStarted and not self.inSettings:
            self.checkInput()
            self.displayButtons()
        elif not self.gameStarted and self.inSettings:
            self.sc.update()

    # def timeUp(self):
    #     self.checkButtons

    # sets a new button as "selected". takes the index of that button wrt the list self.mm.buttons
    def newSelected(self, inc=True):
        #print("selected", self.mm.selected)
        self.mm.buttons[self.mm.selected].selected = False
        self.mm.selected = (self.mm.selected + 1) % len(self.mm.buttons) if inc else (self.mm.selected - 1) % len(self.mm.buttons)
        if inc:
            self.mm.buttons[self.mm.selected].selected = True
        else:
            self.mm.buttons[self.mm.selected].selected = True
        
    def checkInput(self):
        #while (True):
        #gc.pc.timeUpPlayer()
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            #key = pygame.key.get_pressed()
            key = event.key
            #pygame.event.pump()
            #print(key)

            if key == pygame.K_UP: 
                self.newSelected(inc=False)
                print(self.mm.buttons[self.mm.selected].selected)
                print("up")
            elif key == pygame.K_DOWN: 
                self.newSelected(inc=True)
                print("down")
                #print(self.mm.buttons)
                print(self.mm.buttons[self.mm.selected].selected)
            elif key == pygame.K_SPACE: #select the current option
                if self.mm.selected == 0: #start game button is selected
                    print("getting here")
                    self.startGame()
                elif self.mm.selected == 1: #change settings button is selected
                    self.openSettings()
            elif key == pygame.K_ESCAPE: 
                exit()

    def displayExitButton(self):
        pass
    
    def displayPauseButton(self):
        pass

    def pause(self):
        self.paused = not self.paused

    def exit(self):
        exit()

    def startGame(self):
        self.gameStarted = True
        self.createButtons()
        self.gc.startGame()

    def openSettings(self):
        self.inSettings = True

    def returnToMenu(self):
        self.inSettings = False

    def initVolume(self):
        self.sc.volumeUpdate()

    def setGC(self, gameController):
        self.gc = gameController

    def setSC(self, settingsController):
        self.sc = settingsController