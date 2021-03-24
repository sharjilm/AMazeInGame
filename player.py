class PlayerData():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xs = 0
        self.ys = 0
        self.hp = 0
        self.progress = 0
        self.score = 0

class Player():
    def __init__(self):
        self.pd = PlayerData()

    def readPlayer(self):
        return self.pd

    def writePlayer(self, playerData):
        self.pd = playerData
