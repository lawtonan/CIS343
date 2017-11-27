from .Entity import Entity
from weapon import SourStraw, ChocolateBar, NerdBomb
from random import randint

class Person(Entity):
    '''
    A person entity. They help the player by restoring health.
    '''
    def __init__(self):
        '''
        A constucter for Person. Calls the constructor for Entity.
        '''
        super(Person, self).__init__(100, -1)

    def __str__(self):
        '''
        A function that overrides the __str__ function to print the name of the
        Entity.
        '''
        return "Person"

    def takeDamage(self, damage, weapon):
        '''
        Overloading a Entity function for Person. They take 0 damage from all
        sources.

        :param damage:
        :param weapon:
        '''
        super(Person,self).takeDamage(0)

class Zombie(Entity):
    '''
    A zombie entity. A basic monster that takes double damage from sour straws.
    '''
    def __init__(self):
        '''
        A constucter for Zombie. Calls the constructor for Entity.
        '''
        super(Zombie, self).__init__(health=randint(50, 100), attack=randint(0, 10))

    def __str__(self):
        '''
        A function that overrides the __str__ function to print the name of the
        Entity.
        '''
        return "Zombie"

    def takeDamage(self, amount, weapon):
        '''
        Overloading a Entity function for Zombie. They take double damage from
        SourStraw.

        :param damage:
        :param weapon:
        '''
        if type(weapon) is SourStraw:
            print("YES! Zombies take double damage from Sour Straws!")
            damage = amount * 2
        else:
            damage = amount

        super(Zombie, self).takeDamage(damage)

class Vampire(Entity):
    '''
    A vampire entity. A harder monster that takes no damage from chocolate bars.
    '''
    def __init__(self):
        '''
        A constucter for Vampire. Calls the constructor for Entity.
        '''
        super(Vampire, self).__init__(health=randint(100, 200), attack=randint(10, 20))

    def __str__(self):
        '''
        A function that overrides the __str__ function to print the name of the
        Entity.
        '''
        return "Vampire"

    def takeDamage(self, amount, weapon):
        '''
        Overloading a Entity function for Vampire. Vampire takes no damage from
        ChocolateBar.

        :param damage:
        :param weapon:
        '''
        if type(weapon) is ChocolateBar:
            print("OH NO! Vampires take no damage from Chocolate Bars!")
            damage = 0
        else:
            damage = amount
        super(Vampire, self).takeDamage(damage)

class Ghoul(Entity):
    '''
    A ghoul entity. A hard hitting monster that takes 5 times damage from nerd
    bombs.
    '''
    def __init__(self):
        '''
        A constucter for Ghoul. Calls the constructor for Entity.
        '''
        super(Ghoul, self).__init__(health=randint(40, 80), attack=randint(15, 30))

    def __str__(self):
        '''
        A function that overrides the __str__ function to print the name of the
        Entity.
        '''
        return "Ghoul"

    def takeDamage(self, amount, weapon):
        '''
        Overloading a Entity function for Ghoul. They take five times damage from
        NerdBomb.

        :param damage:
        :param weapon:
        '''
        if type(weapon) is NerdBomb:
            print("WOW! Ghouls take five time damage from Nerd Bombs!")
            damage = amount * 5
        else:
            damage = amount

        super(Ghoul, self).takeDamage(damage)

class Werewolf(Entity):
    '''
    A werewolf entity. A difficult monster that takes no damage from chocolate
    bars and sour straws.
    '''
    def __init__(self):
        '''
        A constucter for Werewolf. Calls the constructor for Entity.
        '''
        super(Werewolf, self).__init__(health=200, attack=randint(5, 30))

    def __str__(self):
        '''
        A function that overrides the __str__ function to print the name of the
        Entity.
        '''
        return "Werewolf"

    def takeDamage(self, amount, weapon):
        '''
        Overloading a Entity function for Werewolf. Werewolf takes no damage from
        ChocolateBar and SourStraw.

        :param damage:
        :param weapon:
        '''
        if type(weapon) is ChocolateBar or type(weapon) is SourStraw:
            print("CRAP! Werewolves take no damage from Chocolate Bars or Sour Straws!")
            damage = 0
        else:
            damage = amount
        super(Werewolf, self).takeDamage(damage)

def randMonster():
    '''
    A helper function use to generate a random monster.
    '''
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
