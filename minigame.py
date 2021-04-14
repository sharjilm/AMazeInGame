import minigameContainer

class Minigame():
    def __init__(self):
        #self.md = MinigameData()
        #self.g = [minigameContainer.MinigameData()]
        minigameNum = 5
        self.g = []
        for i in range(5):
            self.g.append(i)
        for i in range(5):
            self.reset(i)


    def readMinigame(self, minigameNum):
        return self.g[minigameNum]

    def writeMinigame(self, minigameNum, minigameData):
        self.g[minigameNum] = minigameData

    def reset(self, minigameNum):
        self.g[minigameNum] = minigameContainer.makeMg(minigameNum)

        # if minigameNum == 0:
        #     self.g[minigameNum] = minigameContainer.makeMg0()
        # elif minigameNum == 1:
        #     self.g[minigameNum] = minigameContainer.makeMg1()
        # elif minigameNum == 2:
        #     self.g[minigameNum] = minigameContainer.makeMg2()
        # elif minigameNum == 3:
        #     self.g[minigameNum] = minigameContainer.makeMg3()
        # elif minigameNum == 4:
        #     self.g[minigameNum] = minigameContainer.makeMg4()
