class MinigameData():    
    def __init__(self):
        self.width = 5
        self.height = 2
        self.tiles = [['0', '1', '0', '1', '0'], ['1', '0', '1', '0', 'w']]
        self.stars = [()]
        self.exit = ()

        self.bots = []
        self.items = []


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
        self.speed = 1
        self.cd = 30
        self.timer = 0
        self.score = -1

class Item():
    def __init__(self):
        self.name = ""
        self.value = 0
        self.x = 0
        self.y = 0
        self.width = 10
        self.height = 10
        self.offset = 10

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

    b = Bot()
    b.name = "1"
    b.track = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for j in b.track:
        b.path.append(j.copy())
    #b.n = 4
    mg.bots.append(b)
    b = Bot()
    b.name = "2"
    b.track = [[6, 0], [0, 6], [-6, 0], [0, -6]]
    b.speed = 2
    for j in b.track:
        b.path.append(j.copy())
    b.score = 0
    mg.bots.append(b)

    i = Item()
    i.value = 100
    i.x = 0
    i.y = 3
    mg.items.append(i)

    return mg