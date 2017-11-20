from observerpattern import observer
from random import randint

class Player(observer):
    def __init__(self):
        self.hp = randint(100,125)
        self.attack = randint(10,20)
        self.weapons = []
        createWeapons()
    def createWeapons():
        weapons.append(HersheyKiss())
        for i in range(9):
            weapons.append(randWeapon())
