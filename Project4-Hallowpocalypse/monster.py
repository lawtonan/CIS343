from observerpattern.observable import Observable
from random import randint

class Monster(Observable):
    def __init__(self, health = 100, strength = 10):
        self.health = health
        self.strength = strength

class Person(Monster):
    def __init__(self):
        super(Monster, self).__init__(self, 100, -1)

class Zombie(Monster):
    def __init__(self):
        super(Monster, self).__init__(self,randint(50,100),randint(0,10))

class Vampire(Monster):
    def __init__(self):
        super(Monster, self).__init__(self, randint(100,200), randint(10,20))

class Ghouls(Monster):
    def __init__(self):
        super(Monster, self).__init__(self, randint(40,80), randint(15,30))

class Werewolve(Monster):
    def __init__(self):
        super(Monster, self).__init__(self,200, randint(0,40))
