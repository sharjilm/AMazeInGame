import random

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
        self.projCD = 10
        self.projTimer = 0
        self.timer = -1 # this refers to minigame 3's main timer
        self.rockets = []

class Projectile():
    def __init__(self):
        self.name = ""

        # self.randomSpeed = random.randint(1, 3)
        self.randomSpeed = 0.25 # #ofBlocks to move/movement update (MUST BE POWER OF 2 (floating point comparison))
        self.randomPosition = random.randint(0, 9)

        # tup is (direction, x, y, xs, ys)
        self.tup = (
        (-1, self.randomPosition, self.randomSpeed, 0), 
        (self.randomPosition, -1, 0, self.randomSpeed), 
        (10, self.randomPosition, -1*self.randomSpeed, 0), 
        (self.randomPosition, 10, 0, -1*self.randomSpeed))

        self.choice = self.tup[random.randint(0, 3)]

        self.x = self.choice[0]
        self.y = self.choice[1]
        self.xs = self.choice[2]
        self.ys = self.choice[3]

        self.width = 10
        self.height = 10
        self.offset = 10
        self.cd = 5 # Projectiles will move every 'self.cd' frames (was 5)
        self.timer = 0
        self.dist = 0
        self.maxDist = 11 // self.randomSpeed

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

class Rocket():
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
                ['0', '1', '0', 'w', '0', '1', 'w', 'w', '0', '1'], 
                ['w', 'w', '1', 'w', 'w', '0', '1', '0', '1', '0'], 
                ['0', 'w', '0', '1', 'w', '1', '0', 'w', 'w', 'w'], 
                ['1', 'w', 'w', '0', 'w', '0', '1', 'w', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', 'w', '0', '1'], 
                ['w', 'w', 'w', '0', '1', '0', '1', 'w', '1', '0'], 
                ['0', '1', '0', '1', 'w', 'w', 'w', 'w', '0', '1'], 
                ['1', 'w', 'w', '0', 'w', '0', '1', '0', 'w', 'w'], 
                ['0', 'w', '0', '1', 'w', '1', 'w', 'w', 'w', '1'], 
                ['1', 'w', '1', '0', '1', '0', 'w', '0', '1', '0']
                ]

    mg.projectiles = []
    mg.timer = 30 * 10 # (30 frames / sec) * 10 seconds = 300 frames 

    mg.entrance = (0, 0)
    mg.exit = (9, 0)

    return mg

def makeMg0():
    mg = MinigameData()
    mg.width = 10
    mg.height = 10
    mg.tiles = [
                ['0', '1', '0', '1', 'w', '1', 'w', '1', '0', '1'], 
                ['w', 'w', '1', 'w', 'w', '0', 'w', '0', '1', '0'], 
                ['0', 'w', '0', '1', 'w', '1', '0', 'w', 'w', '1'], 
                ['1', '0', 'w', '0', 'w', '0', '1', '0', '1', '0'], 
                ['0', 'w', '0', '1', '0', '1', '0', 'w', '0', '1'], 
                ['1', '0', 'w', 'w', '1', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', 'w', 'w', '0', '1'], 
                ['1', 'w', 'w', 'w', 'w', '0', '1', '0', 'w', 'w'], 
                ['0', '1', '0', '1', 'w', 'w', 'w', '1', 'w', '1'], 
                ['1', 'w', '1', '0', 'w', '0', '1', '0', '1', '0']
                ]

    mg.timer = 40 * 30 
    mg.entrance = (0, 0)
    mg.exit = (9, 0)

    i = Item()
    i.name = "d"
    i.value = 0
    i.x = 0
    i.y = 2
    mg.items.append(i)

    i2 = Item()
    i2.name = "de"
    i2.value = 0
    i2.x = 3
    i2.y = 8
    mg.items.append(i2)

    i3 = Item()
    i3.name = "def"
    i3.value = 100
    i3.x = 7
    i3.y = 1
    mg.items.append(i3)

    i4 = Item()
    i4.name = "r"
    i4.value = 100
    i4.x = 9
    i4.y = 8
    mg.items.append(i4)

    i5 = Item()
    i5.name = "colour"
    i5.value = 100
    i5.x = 6
    i5.y = 4
    mg.items.append(i5)

    return mg

def makeMg4():

    mg = MinigameData()
    mg.width = 10
    mg.height = 10
    mg.tiles = [
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0'], 
                ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1'], 
                ['1', '0', '1', '0', '1', '0', '1', '0', '1', '0'], 
                ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], 
                ['1', 'w', '1', '0', '1', 'w', '1', '0', '1', 'w'], 
                ['0', 'w', '0', 'w', '0', 'w', '0', 'w', '0', 'w'], 
                ['1', 'w', '1', 'w', '1', 'w', '1', 'w', '1', 'w'], 
                ['0', 'w', '0', 'w', '0', 'w', '0', 'w', '0', 'w'], 
                ['1', '0', '1', 'w', '1', '0', '1', 'w', '1', '0']
                ]

    mg.timer = 30 * 30 
    mg.entrance = (0, 0)
    mg.exit = (9, 9)

    # create items
    j = 0
    k = 9
    while j < 3:
        for i in range(4):
            item = Item()
            item.name = "d"
            item.x = k
            item.y = i
            item.offset = 0.3
            mg.items.append(item)
        j += 1
        k += 2
        
    return mg

def makeMg1():
    mg = MinigameData()

    mg.end = 1

    return mg