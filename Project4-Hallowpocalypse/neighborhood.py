from home import Home

class Neighborhood(object):
    '''
    A neighborhood class that is used to hold houses for the player to traverse.
    '''
    def __init__(self, height=5, width=5):
        '''
        A constuctor for Neighborhood.
        :param height: the height of the neighborhood.
        :param width: the width of the neighborhood.
        '''
        self.houses = [[Home() for x in range(width)] for y in range(height)]

    def getHouse(self, loc):
        '''
        A getter that returns the house at a specific location.

        :param loc: the location of the house.
        '''
        return self.houses[loc[0]][loc[1]]

    def peekHouse(self, loc):
        '''
        A function to peek into the house.

        :param loc: the location of the house.
        '''
        if self.inBounds(loc):
            return print(self.houses[loc[0]][loc[1]])
        else:
            return "invalid location!"

    def isClear(self):
        '''
        A function to check if the neighborhood is clear.
        '''
        for street in self.houses:
            for house in street:
                if not house.isClear():
                    return False
        return True

    def inBounds(self, loc):
        '''
        A function that checks if the location is in the bounds of the
        neighborhood.
        '''
        if loc[0] in range(0, len(self.houses)) and loc[1] in range(0, len(self.houses[0])):
            return True
        else:
            return False
