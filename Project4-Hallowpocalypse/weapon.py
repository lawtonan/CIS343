from random import randrange
from observerpattern import observable

class Weapon(observable):
    def __init__(self, name, modifier, uses):
        self.name = name
        self.modifier = modifier
        self.uses = uses
    def use():
        uses = uses - 1

class HershyKiss(Weapon):
    def __init__(self):
        super(HershyKiss,self).__init__(self, "HershyKiss", 1, )

class SourStraw(Weapon):
    def __init__(self):
        super(SourStraw,self).__init__(self, "SourStraw", randrange(1,1.75))

class ChocolateBar(Weapon):
    def __init__(self):
        super(ChocolateBar,self).__init__(self, "ChocolateBar", randrange(2,2.4))

class NerdBomb(Weapon):
    def __init__(self):
        super(NerdBomb,self).__init__(self, "NerdBomb", randrange(3.5,5))
