NUMBER_OF_TILES = 100

class Link:
    def __init__(self, fromNumber, toNumber):
        self.fromNumber = fromNumber
        self.toNumber = toNumber
        self.type = 'Snake' if fromNumber > toNumber else 'Ladder'

class Tile:
    def __init__(self, number, nextTile=None, extraTile=None):
        self.number = number
        self.nextTile = nextTile
        self.extraTile = extraTile

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number == other
        return self.number == other.number

    def popExtraTile(self):
        result = self.extraTile
        self.extraTile = None
        return result

class Player:
    def __init__(self, currentTile):
        self.currentTile = currentTile
        self.finish = False

    def move(self, value):
        if self.currentTile.nextTile is None:
            self.finish = True
            return 0

        if value > 0:
            self.currentTile = self.currentTile.nextTile
            return self.move(value - 1)

        if self.currentTile.extraTile is not None:
            print(f"Ho extra move from {self.currentTile.number} to {self.currentTile.extraTile.number} !")
            self.currentTile = self.currentTile.popExtraTile()
        return 0

class TileManager:
    def __init__(self, numberOfTiles, links):
        self.createBoard(numberOfTiles, links)
        
    def createBoard(self, numberOfTiles, links):
        self.tiles = [Tile(0)]
        for i in range(1, numberOfTiles + 1):
            newTile = Tile(i)
            self.tiles[-1].nextTile = newTile
            self.tiles.append(newTile)
            self.applyLink(newTile, links)

    def applyLink(self, currentTile, links):
        for link in links:
            if (link.type == 'Snake' and currentTile.number == link.fromNumber) or (link.type == 'Ladder' and currentTile.number == link.toNumber):
                indexFrom = self.tiles.index(link.fromNumber)
                indexTo = self.tiles.index(link.toNumber)
                self.tiles[indexFrom].extraTile = self.tiles[indexTo]

if __name__ == '__main__':
    print('Are you hable to make it to the end ?')
    links = [
        Link(21, 3),
        Link(4, 75),
        Link(5, 15),
        Link(31, 8),
        Link(98, 12),
        Link(19, 41),
        Link(52, 23),
        Link(28, 50),
        Link(47, 30),
        Link(35, 96),
        Link(76, 41),
        Link(44, 82),
        Link(53, 94),
        Link(59, 95),
        Link(81, 62),
        Link(88, 67),
        Link(70, 91),
    ]

    tileManager = TileManager(NUMBER_OF_TILES, links)
    playerOne = Player(tileManager.tiles[0])

    while not playerOne.finish:
        diceResult = -1
        print(f"You are in the tile number : {playerOne.currentTile.number}")
        while diceResult < 1 or diceResult > 6:
            try:
                diceResult = int(input("Enter the dice value of your choice (between 1 and 6) : "))
            except:
                quit = input("Wrong input, do you want to quit ?")
                if quit.find('y'):
                    exit(0)
                diceResult = -1
        playerOne.move(diceResult)
    print("Victory !! You make it threw the end !")
    exit(0)