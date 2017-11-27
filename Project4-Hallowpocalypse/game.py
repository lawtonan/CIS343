from entities.player import Player
from observerpattern.observer import Observer
from neighborhood import Neighborhood


class Game(Observer):
    '''
    A game object that is used to play the game. The game has a player and a
    neighborhood, while storing the players location the player can attack that
    location.
    '''
    def __init__(self, size = 5):
        '''
        A constructor for game. Creates the player and neighborhood and stores
        information regarding them.

        :param size: The size of the neighborhood. (Defaults to 5x5)
        '''
        self.player = Player()
        self.player.add_observer(self)
        self.playerLoc = (0, 0)
        self.neighborhood = Neighborhood(size, size)
        self.isPlaying = True

    def receiveUpdate(self, info=None):
        '''
        An abstract function that is impimented by game to get an update when the
        player still is playing.
        '''
        self.isPlaying = False

    def getStatus(self):
        '''
        A getter that returns the game status.
        '''
        return self.isPlaying

    def getPlayer(self):
        '''
        A getter that return the player
        '''
        return self.player

    def getNeighborhood(self):
        '''
        A getter that returns the neighborhood.
        '''
        return self.neighborhood

    def getPlayerLoc(self):
        '''
        A getter that returns the player location.
        '''
        return self.playerLoc

    def move(self, direction):
        '''
        A move function that moves the player location in four directions.
        Returns boolean values to determine if the move was possible or not.

        :param direction: a direction (north, south, east, west)
        '''
        if not self.isPlaying:
            return False

        if direction == "north":
            newLoc = (self.playerLoc[0] - 1, self.playerLoc[1])
            if self.neighborhood.inBounds(newLoc):
                self.playerLoc = newLoc
                return True
        elif direction == "south":
            newLoc = (self.playerLoc[0] + 1, self.playerLoc[1])
            if self.neighborhood.inBounds(newLoc):
                self.playerLoc = newLoc
                return True
        elif direction == "east":
            newLoc = (self.playerLoc[0], self.playerLoc[1] + 1)
            if self.neighborhood.inBounds(newLoc):
                self.playerLoc = newLoc
                return True
        elif direction == "west":
            newLoc = (self.playerLoc[0], self.playerLoc[1] -1)
            if self.neighborhood.inBounds(newLoc):
                self.playerLoc = newLoc
                return True

        return False

    def attackHouse(self, loc, weaponNum):
        '''
        An attack function that attacks all monsters in a house.

        :param loc: The location being attacked.
        :param weaponNum: the weapon used to attack.
        '''
        if not self.isPlaying:
            return

        self.player.attackAll(self.neighborhood.getHouse(loc), weaponNum)
        self.neighborhood.getHouse(loc).dealDamage(self.player)

        if self.getNeighborhood().isClear():
            self.isPlaying = False
