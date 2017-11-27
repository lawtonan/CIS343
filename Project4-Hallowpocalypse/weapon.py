from random import randint, uniform
from observerpattern.observable import Observable

class Weapon(Observable):
    def __init__(self, name, modifier, uses):
        self.name = name
        self.modifier = modifier
        self.uses = uses
        super(Weapon, self).__init__()

    def __str__(self):
        return "{} \t Durability: {}".format(self.name, self.uses)

    def getName(self):
        return self.name

    def use(self, amount):
        if self.name == "HersheyKiss":
            return amount
        if self.durability > 0:
            modAmount = amount * self.modifier
            self.uses = self.uses - 1
            return modAmount
        else:
            return 0

    def checkStatus(self):
        if self.durability <= 0 and not self.name == "HersheyKiss":
            self.sendUpdate(self)
            self.remove_all_observers()


class HersheyKiss(Weapon):
    def __init__(self):
        super(HersheyKiss,self).__init__("HersheyKiss", 1, -1)

class SourStraw(Weapon):
    def __init__(self):
        super(SourStraw,self).__init__("SourStraw", uniform(1,1.75), 2)

class ChocolateBar(Weapon):
    def __init__(self):
        super(ChocolateBar,self).__init__("ChocolateBar", uniform(2,2.4), 4)

class NerdBomb(Weapon):
    def __init__(self):
        super(NerdBomb,self).__init__("NerdBomb", uniform(3.5,5), 1)

def randWeapons(amount, player):
    weapons = []
    weapons.append(HersheyKiss())
    for i in range(amount - 1):
        weapons.append(randWeapon())
        weapons[len(weapons) - 1].add_observer(player)
    return weapons

def randWeapon():
    weaponInt = randint(0, 2)
    if weaponInt == 0:
        return SourStraw()
    elif weaponInt == 1:
        return ChocolateBar()
    elif weaponInt == 2:
        return NerdBomb()
