import gameController
import pygame
import time

def main():
    gc = gameController.GameController()
    gc.startGame()
    clock = pygame.time.Clock()


    while(True):
        gc.pc.timeUpPlayer()
        #print("who")
        clock.tick(30) # 30fps

main()
        
