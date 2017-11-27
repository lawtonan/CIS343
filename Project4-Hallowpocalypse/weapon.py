from random import randint, uniform
from observerpattern.observable import Observable

class Weapon(Observable):
    '''
    A weapon class that is used by player.
    '''
    def __init__(self, name, modifier, uses):
        '''
        A contructor for weapon.

        :param name: the name of the weapon.
        :param modifer: the damage modifier.
        :param uses: the uses of the weapon.
        '''
        self.name = name
        self.modifier = modifier
        self.uses = uses
        super(Weapon, self).__init__()

    def __str__(self):
        '''
        A function that overloads the __str__ function to print the weapon
        and it's uses.
        '''
        return "{} \t uses: {}".format(self.name, self.uses)

    def getName(self):
        '''
        A getter that returns the name of the weapon.
        '''
        return self.name

    def use(self, amount):
        '''
        A use function that returns the damage of the weapon.

        :param amount: the modifier
        '''
        if self.name == "HersheyKiss":
            return amount
        if self.uses > 0:
            modAmount = amount * self.modifier
            self.uses = self.uses - 1
            return modAmount
        else:
            return 0

    def checkStatus(self):
        '''
        A method overloaded from observable to update when the weapon breaks.
        '''
        if self.uses <= 0 and not self.name == "HersheyKiss":
            self.sendUpdate(self)
            self.remove_all_observers()


class HersheyKiss(Weapon):
    '''
    A HersheyKiss class. This class has a damage modifer of 1 and infinite uses.
    '''
    def __init__(self):
        '''
        A constuctor for HersheyKiss. Calls the constuctor for weapon.
        '''
        super(HersheyKiss,self).__init__("HersheyKiss", 1, -1)

class SourStraw(Weapon):
    '''
    A SourStraw class. This class has a damage modifer of 1 - 1.75 and 2 uses.
    '''
    def __init__(self):
        '''
        A constuctor for SourStraw. Calls the constuctor for weapon.
        '''
        super(SourStraw,self).__init__("SourStraw", uniform(1,1.75), 2)

class ChocolateBar(Weapon):
    '''
    A ChocolateBar class. This class has a damage modifer of 2 - 2.4 and 4 uses.
    '''
    def __init__(self):
        '''
        A constuctor for ChocolateBar. Calls the constuctor for weapon.
        '''
        super(ChocolateBar,self).__init__("ChocolateBar", uniform(2,2.4), 4)

class NerdBomb(Weapon):
    '''
    A NerdBomb class. This class has a damage modifer of 3.5 - 5 and 5 uses
    '''
    def __init__(self):
        '''
        A constuctor for NerdBomb. Calls the constuctor for weapon.
        '''
        super(NerdBomb,self).__init__("NerdBomb", uniform(3.5,5), 1)

def randWeapons(amount, player):
    '''
    A function that creates a list of random weapons.
    '''
    weapons = []
    weapons.append(HersheyKiss())
    for i in range(amount - 1):
        weapons.append(randWeapon())
        weapons[len(weapons) - 1].add_observer(player)
    return weapons

def randWeapon():
    '''
    A function that creates a random weapon.
    '''
    weaponInt = randint(0, 2)
    if weaponInt == 0:
        return SourStraw()
    elif weaponInt == 1:
        return ChocolateBar()
    elif weaponInt == 2:
        return NerdBomb()
