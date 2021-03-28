class MinigameData():    
    def __init__(self):
        self.width = 5
        self.height = 2
        self.tiles = [['0', '1', '0', '1', '0'], ['1', '0', '1', 'w', '1']]
        self.stars = [()]
        self.entrance = (0, 0)
        self.exit = (4, 1)
        self.end = 0

        self.bots = []
        self.items = []
        self.projectiles = []
        self.projCD = 90
        self.projTimer = 0
        self.timer = -1 # this refers to minigame 3's main timer

class Projectile():
    def __init__(self):
        self.name = ""
        self.x = -1
        self.y = 5
        self.xs = 1
        self.ys = 0
        self.width = 10
        self.height = 10
        self.offset = 10
        self.cd = 30
        self.timer = 0
        self.dist = 0

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

def makeMg2():
    mg = MinigameData()
    mg.width = 10
    mg.height = 10
    mg.tiles = [
                ['0', '1', '0', '1', '0', '1', '0', 'w', 'w', 'w'], 
                ['1', '0', '1', '0', 'w', 'w', 'w', 'w', '1', 'w'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', 'w'], 
                ['1', '0', '1', '0', 'w', 'w', 'w', 'w', '1', 'w'], 
                ['0', '1', '0', '1', '0', '1', '0', 'w', '0', 'w'], 
                ['1', '0', '1', '0', 'w', '0', '1', 'w', '1', 'w'], 
                ['0', 'w', '0', '1', '0', '1', '0', '1', '0', 'w'], 
                ['1', 'w', '1', '0', 'w', '0', '1', '0', '1', 'w'], 
                ['0', 'w', '0', '1', '0', '1', 'w', 'w', '0', 'w'], 
                ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
                ]

    b = Bot()
    b.name = "1"
    b.track = [[6, 0], [0, 6], [-6, 0], [0, -6]]
    b.speed = 2
    for j in b.track:
        b.path.append(j.copy())
    b.score = 0
    b.cd = 15
    mg.bots.append(b)

    b = Bot()
    b.name = "2"
    b.track = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for j in b.track:
        b.path.append(j.copy())
    mg.bots.append(b)


    i = Item()
    i.name = "d"
    i.value = 100
    i.x = 0
    i.y = 2
    mg.items.append(i)

    # i = Item()
    # i.name = "d"
    # i.value = 100
    # i.x = 8
    # i.y = 1
    # mg.items.append(i)

    # i = Item()
    # i.name = "r"
    # i.value = 200
    # i.x = 8
    # i.y = 8
    # mg.items.append(i)

    # i = Item()
    # i.name = "r"
    # i.value = 200
    # i.x = 0
    # i.y = 8
    # mg.items.append(i)

    # i = Item()
    # i.name = "r"
    # i.value = 200
    # i.x = 2
    # i.y = 0
    # mg.items.append(i)

    mg.entrance = (0, 0)
    mg.exit = (0, 0)

    return mg

def makeMg3():
    mg = MinigameData()
    mg.width = 10
    mg.height = 10
    mg.tiles = [
                ['0', '1', '0', '1', '0', '1', '0', '1', '1', '0'], 
                ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '0'], 
                ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '0'], 
                ['1', '0', '1', '0', '1', '0', '1', '1', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '0'], 
                ['1', '1', '1', '0', '1', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '1', '1', '0', '0'], 
                ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0']
                ]

    mg.projectiles = []
    mg.timer = 30 * 30

    mg.entrance = (1, 1)
    mg.exit = (1, 1)

    return mg

def makeMg0():
    mg = MinigameData()

    mg.end = -1

    return mg

def makeMg1():
    mg = MinigameData()

    mg.end = -1

    return mg

def makeMg4():
    mg = MinigameData()

    mg.end = -1

    return mg