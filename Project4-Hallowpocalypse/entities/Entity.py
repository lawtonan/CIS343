from observerpattern.observable import Observable

class Entity(Observable):

    def __init__(self, health = 100, attack = 10):
        self.health = health
        self.maxHealth = health
        self.attack = attack

        super(Entity, self).__init__()

    def sendUpdate(self):
        super(Entity, self).sendUpdate(info=self)

    def isDead(self):
        if self.health <= 0:
            return True
        return False

    def takeDamage(self, amount):
        self.health = self.health - amount

        if self.health < 0:
            self.health = 0
        if self.health > self.maxHealth:
            self.health = self.maxHealth

        self.printDamage(amount)

        if self.isDead():
            self.sendUpdate()
            self.remove_all_observers()

    def printDamage(self, amount):
        if not self.isDead():
            print("{} takes {} damage! \t current health: {}".format(self, amount, self.health))
        else:
            print("{} takes {} damage! \t current health: {}".format(self, amount, self.health))
            print("{} is defeated and transforms back into a human!".format(self))

    def dealDamage(self, target, modifier=1):
        target.takeDamage(self.attack * modifier)
