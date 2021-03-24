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
        self.name = ""
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.offset = 10
        self.track = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.path = []
        self.cd = 30
        self.timer = 0

def makeMg3():
    mg = MinigameData()
    mg.width = 10
    mg.height = 10
    mg.tiles = [
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', 'w', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', 'w', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', 'w', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', 'w', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', 'w', '0', '1', '0', '1', '0']
                ]
    mg.stars = [()]
    mg.exit = ()

    mg.bots = []
    b = Bot()
    b.name = "1"
    b.track = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for j in b.track:
        b.path.append(j.copy())
    #b.n = 4
    mg.bots.append(b)
    b = Bot()
    b.name = "2"
    b.track = [[5, 0], [0, 5], [-5, 0], [0, -5]]
    for j in b.track:
        b.path.append(j.copy())
    mg.bots.append(b)

    return mg