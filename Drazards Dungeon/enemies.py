class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw enemy objects.")

    def __str__(self):
        return self.name


    def is_alive(self):
        return self.hp > 0

class SpookySkeleton(Enemy):
    def __init__(self):
        self.name = "Spooky Skeleton"
        self.hp = 10
        self.damage = 6


class GhastlyGhost(Enemy):
    def __init__(self):
        self.name = "Ghastly Ghost"
        self.hp = 30
        self.damage = 2


class Daniel(Enemy):
    def __init__(self):
        self.name = "Rock Spider"
        self.hp = 60
        self.damage = 1


class BeastlyBear(Enemy):
    def __init__(self):
        self.name = "Beastly Bear"
        self.hp = 50
        self.damage = 4
