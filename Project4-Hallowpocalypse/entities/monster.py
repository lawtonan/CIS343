from .Entity import Entity
from weapon import SourStraw, ChocolateBar, NerdBomb
from random import randint

class Person(Entity):
    def __init__(self):
        super(Person, self).__init__(100, -1)
    def __str__(self):
        return "Person"
    def takeDamage(self, damage, weapon):
        super(Person,self).takeDamage(0)

class Zombie(Entity):
    def __init__(self):
        super(Zombie, self).__init__(health=randint(50, 100), attack=randint(0, 10))

    def __str__(self):
        return "Zombie"

    def takeDamage(self, amount, weapon):
        if type(weapon) is SourStraw:
            print("Zombies take Double damage from Sour Straws")
            damage = amount * 2
        else:
            damage = amount

        super(Zombie, self).takeDamage(damage)

class Vampire(Entity):
    def __init__(self):
        super(Vampire, self).__init__(health=randint(100, 200), attack=randint(10, 20))

    def __str__(self):
        return "Vampire"

    def takeDamage(self, amount, weapon):
        if type(weapon) is ChocolateBar:
            print("Vampires take no damage from Chocolate Bars")
            damage = 0
        else:
            damage = amount
        super(Vampire, self).takeDamage(damage)

class Ghoul(Entity):
    def __init__(self):
        super(Ghoul, self).__init__(health=randint(40, 80), attack=randint(15, 30))

    def __str__(self):
        return "Ghoul"

    def takeDamage(self, amount, weapon):
        if type(weapon) is NerdBomb:
            damage = amount * 5
        else:
            damage = amount

        super(Ghoul, self).takeDamage(damage)

class Werewolf(Entity):
    def __init__(self):
        super(Werewolf, self).__init__(health=200, attack=randint(5, 30))

    def __str__(self):
        return "Werewolf"

    def takeDamage(self, amount, weapon):
        if type(weapon) is ChocolateBar or type(weapon) is SourStraw:
            print("Werewolves take no damage from Chocolate Bars or Sour Straws")
            damage = 0
        else:
            damage = amount
        super(Werewolf, self).takeDamage(damage)

def randMonster():
    monsterInt = randint(0, 4)

    if(monsterInt == 0):
        return Person()
    elif(monsterInt == 1):
        return Zombie()
    elif(monsterInt == 2):
        return Vampire()
    elif(monsterInt == 3):
        return Ghoul()
    elif(monsterInt == 4):
        return Werewolf()
    else:
        return None
