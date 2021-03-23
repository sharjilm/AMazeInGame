class MapData():
    def __init__(self):
        self.width = 5
        self.height = 5
        self.tiles = [['0', '1', '0', '1', '0'], ['1', '0', '1', '0', '1'], ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'], ['0', '1', '0', '1', '0']]
        self.stars = [()]
        self.exit = ()

class Map():
    def __init__(self):
        self.md = MapData()

    def readMap(self):
        return self.md

    def writeMap(self, mapData):
        self.md = mapData
