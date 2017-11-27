from observerpattern.observer import Observer
from random import randint
from entities import monster

class Home(Observer):
    '''
    A home class that holds monsters.
    '''
    def __init__(self):
        '''
        A constucter for home.
        '''
        self.monsters = self.createMonsters()

    def __str__(self):
        '''
        A function that overloads the __str__ function to print the house contents.
        '''
        s = "\nHouse Contains: \n"
        if len(self.monsters) == 0:
            s = s + "Nothing\n"
        for mon in self.monsters:
            s = s + "{} \n".format(mon)
        return s

    def getMonsterlist(self):
        '''
        A getter that returns the monsters.
        '''
        return self.monsters

    def isClear(self):
        '''
        A function that checks if all monsters have been converted.
        '''
        for mon in self.monsters:
            if not(type(mon) is monster.Person):
                return False
        return True

    def receiveUpdate(self, info):
        '''
        Implementing the abstract from Observer. It turns a monster to a person
        when it updates.
        '''
        if info in self.monsters:
            self.monsters[self.monsters.index(info)] = monster.Person()

    def dealDamage(self, player):
        '''
        A function used to deal damage to all monsters as long as the monster is
        not dead.
        '''
        for mon in self.monsters:
            if not player.isDead():
                mon.dealDamage(player)

    def createMonsters(self):
        '''
        A function used to create a list of monsters.
        '''
        monsterList = []
        for i in range(0, randint(0, 10)):
            monsterList.append(monster.randMonster())
            monsterList[len(monsterList) - 1].add_observer(self)
        return monsterList
