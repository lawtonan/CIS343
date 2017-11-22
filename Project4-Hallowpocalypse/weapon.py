from random import randrange
from observerpattern import observable

class Weapon(observable):
    def __init__(self, name, modifier, uses):
        self.name = name
        self.modifier = modifier
        self.uses = uses
    def use():
        uses = uses - 1
        if uses < 0 and not type(HersheyKiss):
            update()
    def randWeapon():
        for i in randrange(3):
            if i == 0:
                return SourStraw()
            if i == 1:
                return ChocolateBar()
            if i == 2:
                return NerdBomb()
    def getModifier():
        return modifier

class HersheyKiss(Weapon):
    def __init__(self):
        super(HersheyKiss,self).__init__(self, "HersheyKiss", 1, -1)

class SourStraw(Weapon):
    def __init__(self):
        super(SourStraw,self).__init__(self, "SourStraw", randrange(1,1.75))

class ChocolateBar(Weapon):
    def __init__(self):
        super(ChocolateBar,self).__init__(self, "ChocolateBar", randrange(2,2.4))

class NerdBomb(Weapon):
    def __init__(self):
        super(NerdBomb,self).__init__(self, "NerdBomb", randrange(3.5,5))
