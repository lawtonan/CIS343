from home import Home

class Neighborhood(object):
    def __init__(self, height=5, width=5):
        self.houses = [[Home() for x in range(width)] for y in range(height)]

    def getHouse(self, loc):
        return self.houses[loc[0]][loc[1]]

    def peekHouse(self, loc):
        if self.inBounds(loc):
            return print(self.houses[loc[0]][loc[1]])
        else:
            return "invalid location!"

    def isClear(self):
        for street in self.houses:
            for house in street:
                if not house.isClear():
                    return False
        return True

    def inBounds(self, loc):
        if loc[0] in range(0, len(self.houses)) and loc[1] in range(0, len(self.houses[0])):
            return True
        else:
            return False
