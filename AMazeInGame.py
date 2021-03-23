import gameController

def main():
    gc = gameController.GameController()
    print("what")
    gc.startGame()
    print("hmm")

    while(True):
        gc.pc.timeUpPlayer()
        #print("who")
        pass

main()
        
