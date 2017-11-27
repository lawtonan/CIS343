from entities.player import Player
from observerpattern.observer import Observer
from neighborhood import Neighborhood


class Game(Observer):
    def __init__(self, size = 5):
        self.player = Player()
        self.player.add_observer(self)
        self.playerLoc = (0, 0)
        self.neighborhood = Neighborhood(size, size)
        self.isPlaying = True

    def receiveUpdate(self, info=None):
        self.isPlaying = False

    def getStatus(self):
        return self.isPlaying

    def getPlayer(self):
        return self.player

    def getNeighborhood(self):
        return self.neighborhood

    def getPlayerLoc(self):
        return self.playerLoc

    def move(self, direction):
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
        if not self.isPlaying:
            return

        self.player.attackAll(self.neighborhood.getHouse(loc), weaponNum)
        self.neighborhood.getHouse(loc).dealDamage(self.player)

        if self.getNeighborhood().isClear():
            self.isPlaying = False
