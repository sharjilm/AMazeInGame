import minigameContainer

class Minigame():
    def __init__(self):
        #self.md = MinigameData()
        #self.g = [minigameContainer.MinigameData()]
        self.g = [minigameContainer.MinigameData(), 
                minigameContainer.MinigameData(),
                minigameContainer.makeMg2(), 
                minigameContainer.makeMg3(),
                minigameContainer.MinigameData()]


    def readMinigame(self, minigameNum):
        return self.g[minigameNum]

    def writeMinigame(self, minigameNum, minigameData):
        self.g[minigameNum] = minigameData

    def reset(self, minigameNum):
        if minigameNum == 2:
            self.g[minigameNum] = minigameContainer.makeMg2()
        elif minigameNum == 3:
            self.g[minigameNum] = minigameContainer.makeMg3()
