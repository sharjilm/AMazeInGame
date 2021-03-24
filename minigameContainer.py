class MinigameData():    
    def __init__(self):
        self.width = 5
        self.height = 2
        self.tiles = [['0', '1', '0', '1', '0'], ['1', '0', '1', '0', 'w']]
        self.stars = [()]
        self.exit = ()

        self.bots = [Bot()]

class Bot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.offset = 10
        self.path = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.p = 0
        self.n = 4
        self.cd = 30
        self.timer = 0