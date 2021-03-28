import minigameContainer

class Minigame():
    def __init__(self):
        #self.md = MinigameData()
        #self.g = [minigameContainer.MinigameData()]
        self.g = [minigameContainer.makeMg0(), 
                minigameContainer.makeMg1(),
                minigameContainer.makeMg2(), 
                minigameContainer.makeMg3(),
                minigameContainer.makeMg4()]


    def readMinigame(self, minigameNum):
        return self.g[minigameNum]

    def writeMinigame(self, minigameNum, minigameData):
        self.g[minigameNum] = minigameData

    def reset(self, minigameNum):
        if minigameNum == 0:
            self.g[minigameNum] = minigameContainer.makeMg0()
        elif minigameNum == 1:
            self.g[minigameNum] = minigameContainer.makeMg1()
        elif minigameNum == 2:
            self.g[minigameNum] = minigameContainer.makeMg2()
        elif minigameNum == 3:
            self.g[minigameNum] = minigameContainer.makeMg3()
        elif minigameNum == 4:
            self.g[minigameNum] = minigameContainer.makeMg4()
