
class Weapon():
    def __init__(self, name, modifier):
        self.name = name
        self.modifier = modifier

class HershyKiss(Weapon):
    def __init__(self):
        super(self, "HershyKiss", 1)

class SourStraw(Weapon):
    def __init__(self):
        pass

class ChocolateBar(Weapon):
    def __init__(self):
        pass

class NerdBomb(Weapon):
    def __init__(self):
        pass
