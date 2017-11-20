from observerpattern.observer import Observer
from random import randint
from random import randrange

class Home(Observer):
    def __init__(self):
        self.monsters = []
        createMonsters(randint(0,10))
    def createMonsters(num):
        for i in range(num):
            monsters.append(randMonter())
