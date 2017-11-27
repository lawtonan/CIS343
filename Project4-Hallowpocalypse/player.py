import Entity
from observerpattern.observer import Observer
from observerpatter.observable import Observable
from random import randint
import weapon

class Player(Entity, Observer, Observable):
    def __init__(self):

        self.name = "Player"
        self.weapons = Weapons.randWeapons(10,self)
        Entity.__init__(self, attack=randint(10, 20))
        Observable.__init__(self)

    def __str__(self):
        return self._name

    def receiveUpdate(self, info):
        if info in self._weapons:
            print("Your uses for {} reaches 0 and falls apart!".format(info.getName()))
            self.weapons.remove(info)
    def attack(self, house, weaponNum):
        if weaponNum < 0 or weaponNum >= len(self.weapons):
            print("Weapon does not exist!")
            return
        monsters = house.getMonsterlist()
        damage = self.weapons[weaponNum].use(self.attack)
        for mon in monsters:
            mon.takeDamage(damage, self._weapons[weaponNum])
        self.weapons[weaponNum].checkStatus()

    def dealDamage(self, target, weaponNum):
        if weaponNum < 0 or weaponNum >= len(self._weapons):
            print("Weapon does not exist!")
            return
        target.takeDamage(self._weapons[weaponNum].use(self._attack), self._weapons[weaponNum])

    def printDamage(self, amount):
        if not self.isDead():
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
        else:
            print("{} takes {} damage! \t current health: {}".format(self, amount, self._health))
            print("{} is defeated and transforms into a {}!".format(self, "Monster"))

    def printWeapons(self):
        [print("{}: {}".format(i, weap)) for i, weap in enumerate(self._weapons)]

    def getWeapon(self, weaponNum):
        return self._weapons[weaponNum]
