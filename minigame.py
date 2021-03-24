import minigameContainer

class Minigame():
    def __init__(self):
        #self.md = MinigameData()
        self.g = [minigameContainer.MinigameData()]
        self.g = [minigameContainer.makeMg3()]


    def readMinigame(self, minigameNum):
        return self.g[minigameNum]

    def writeMinigame(self, minigameNum, minigameData):
        self.g[minigameNum] = minigameData
