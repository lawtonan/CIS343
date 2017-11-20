from observerpattern.observable import Observable
from random import randint

class Monster(Observable):
    ''' Docs Here '''
    def __init__(self, health = 100, strength = 10):
        self.health = health
        self.strength = strength
    def takeDamage(self, damage, weapon):
        health = health - damage
        if (health < 0):
            update(self)
    def randMonter():
        for num in randrange(5):
            if (num == 0):
                person = Person()
                return person
            if (num == 1):
                zombie = Zombie()
                return zombie
            if (num == 2):
                vampire = Vampire()
                return vampire
            if (num == 3):
                ghoul = Gouhl()
                return ghoul
            if (num == 4):
                werewolf = Werewolf()
                return werewolf

class Person(Monster):
    def __init__(self):
        super(Person, self).__init__(self, 100, -1)
    def takeDamage(self, damage, weapon):
        super(Person,self).takeDamage(self, 0)

class Zombie(Monster):
    def __init__(self):
        super(Zombie, self).__init__(self,randint(50,100),randint(0,10))
    def takeDamage(self, damage, weapon):
        if (type(weapon) is SourStraw):
            super(Zombie,self).takeDamage(self, 2*damage, weapon)
        else:
            super(Zombie,self).takeDamage(self, damage, weapon)

class Vampire(Monster):
    def __init__(self):
        super(Vampire, self).__init__(self, randint(100,200), randint(10,20))
    def takeDamage(self, damage, weapon):
        if (type(weapon) is ChocolateBar):
            super(Vampire,self).takeDamage(self, 0, weapon)
        else:
            super(Vampire,self).takeDamage(self, damage, weapon)

class Ghoul(Monster):
    def __init__(self):
        super(Ghoul, self).__init__(self, randint(40,80), randint(15,30))
    def takeDamage(self, damage, weapon):
        if (type(weapon) is NerdBomb):
            super(Ghoul,self).takeDamage(self, 5*damage, weapon)
        else:
            super(Ghoul,self).takeDamage(self, damage, weapon)

class Werewolf(Monster):
    def __init__(self):
        super(Werewolf, self).__init__(self,200, randint(0,40))
    def takeDamage(self, damage, weapon):
        if (type(weapon) is ChocolateBar or type(weapon) is SourStraw):
            super(Zombie,self).takeDamage(self, 0*damage, weapon)
        else:
            super(Zombie,self).takeDamage(self, damage, weapon)
