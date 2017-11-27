from observerpattern.observable import Observable

class Entity(Observable):
    '''
    This is an Entity class. This class is used for anything that deals or takes
    damage.
    '''
    def __init__(self, health = 100, attack = 10):
        '''
        This is a constructor for Entity

        :param health: the total health of the Entity
        :param attack: base attack of the Entity
        '''
        self.health = health
        self.maxHealth = health
        self.attack = attack
        #calls the Observable constructor.
        super(Entity, self).__init__()

    def sendUpdate(self):
        """
        Overloaded sendUpdate function from Observable. Used when we die so the
        Observer can update the variables.
        """
        super(Entity, self).sendUpdate(info=self)

    def isDead(self):
        """
        A boolean helper function that is used to check if the Entity is dead.
        """
        if self.health <= 0:
            return True
        return False

    def takeDamage(self, amount):
        """
        A general take damage function. Is overloaded when taking damage is
        changed per Entity.

        :param amount: the amount of damage
        """
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
        """
        A helper function used to make printing the damage from an entity look
        nicer.

        :param amount: the amount of damage
        """
        if not self.isDead():
            print("{} takes {} damage! \t current health: {}".format(self, amount, self.health))
        else:
            print("{} takes {} damage! \t current health: {}".format(self, amount, self.health))
            print("{} is defeated and transforms back into a human!".format(self))

    def dealDamage(self, target, modifier=1):
        """
        A function used to deal damage to an entity.

        :param target: the target of the damage
        :param modifer: the damage multiplier, defaults to 1 when not used.
        """
        target.takeDamage(self.attack * modifier)
