class PlayerData():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xs = 0
        self.ys = 0
        self.maxHP = 3 # should be 100 (or something higher than 10)
        self.hp = self.maxHP
        self.stars = 0
        self.score = -1
        self.time = 0

class Player():
    def __init__(self):
        self.pd = PlayerData()

    def readPlayer(self):
        return self.pd

    def writePlayer(self, playerData):
        self.pd = playerData
