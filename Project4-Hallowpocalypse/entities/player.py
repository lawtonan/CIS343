from .Entity import Entity
from observerpattern.observer import Observer
from observerpattern.observable import Observable
from random import randint
import weapon

class Player(Entity, Observer, Observable):
    '''
    A player entity. This is the player and attacks and is attacked by monsters.
    '''
    def __init__(self):
        '''
        The contructor for Player. Calls the constructors for both Entity and
        Observable.
        '''
        self.name = "Player"
        self.weapons = weapon.randWeapons(10,self)
        Entity.__init__(self, attack=randint(10, 20))
        Observable.__init__(self)

    def __str__(self):
        '''
        A function that overloads the __str__ function for player. Returns
        "Player" always. (can be changed to add player name functionality)
        '''
        return self.name

    def receiveUpdate(self, info):
        '''
        Implimented abstract function from Observer. Used to know when weapons reach
        0 uses.

         :param info: A weapon to check for.
        '''
        if info in self.weapons:
            print("Your uses for {} reaches 0 and falls apart!".format(info.getName()))
            self.weapons.remove(info)

    def attackAll(self, house, weaponNum):
        '''
        A function used to attack all monsters within a house.

        :param house: the house being attacked.
        :param weaponNum: the weapon modifier.
        '''
        if weaponNum < 0 or weaponNum >= len(self.weapons):
            print("Weapon does not exist!")
            return
        monsters = house.getMonsterlist()
        damage = self.weapons[weaponNum].use(self.attack)
        for mon in monsters:
            mon.takeDamage(damage, self.weapons[weaponNum])
        self.weapons[weaponNum].checkStatus()

    def dealDamage(self, target, weaponNum):
        '''
        A function used to deal damage to a target.

        :param target: the target taking damage.
        :param weaponNum: the weapon modifier.
        '''
        if weaponNum < 0 or weaponNum >= len(self.weapons):
            print("Weapon does not exist!")
            return
        target.takeDamage(self.weapons[weaponNum].use(self.attack), self.weapons[weaponNum])

    def printDamage(self, amount):
        '''
        A helper function used to print the damage values for player.

        :param amount: the amount of damage.
        '''
        if not self.isDead():
            print("OUCH! You take {} damage! \t current health: {}\n".format(amount, self.health))
        else:
            print("OUCH! You take {} damage! \t current health: {}\n".format(amount, self.health))
            print("OH NO! You are defeated!\n")

    def printWeapons(self):
        '''
        A helper function used to print the player's weapons. 
        '''
        [print("{}: {}".format(i, weap)) for i, weap in enumerate(self.weapons)]

    def getWeapon(self, weaponNum):
        '''
        A getter to get a certain weapon from player.

        :param weaponNum: the weapon wanted
        '''
        return self.weapons[weaponNum]
