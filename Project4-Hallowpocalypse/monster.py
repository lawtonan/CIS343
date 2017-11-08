from Project4-Hallowpocalypse.observable import Observable
from random imort randint

class Monster(Observable):
    def __init__(self, health = 100, strength = 10):
        self.health = health
        self.strength = strength

class Person(Monster):
    def __init__(self):
        super(self, 100, -1)

class Zombie(Monster):
    def __init__(self):
        super(self,health(),strength())
    def health():
        return randint(50,100)
    def strength():
        return randint(0,10)

class Vampire(Monster):
    def __init__(self):
        super(self,health(),strength())
    def health():
        return randint(100,200)
    def strength():
        return randint(10,20)

class Ghouls(Monster):
    def __init__(self):
        super(self,health(),strength())
    def health():
        return randint(40,80)
    def strength():
        return randint(15,30)

class Werewolve(Monster):
    def __init__(self):
        super(self,200,strength())
    def strength():
        return randint(0,40)
