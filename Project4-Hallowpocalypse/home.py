from observerpattern.observer import Observer
import random
from entities import monster

class Home(Observer):
    def __init__(self):
        self.monsters = self.createMonsters()

    def __str__(self):
        s = "\nHouse Contains: \n"
        if len(self._monsters) == 0:
            s = s + "Nothing\n"
        for mon in self._monsters:
            s = s + "{} \n".format(mon)
        return s

    def getMonsterlist(self):
        return self.monsters

    def isClear(self):
        for mon in self.monsters:
            if not(type(mon) is Monsters.Person):
                return False
        return True

    def receiveUpdate(self, info):
        if info in self._monsters:
            self._monsters[self._monsters.index(info)] = Monsters.Person()

    def dealDamage(self, player):
        for mon in self.monsters:
            if not player.isDead():
                mon.dealDamage(player)

    def createMonsters(num):
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(Monsters.randMonster())
            monsterList[len(monsterList) - 1].add_observer(self)
        return monsterList
