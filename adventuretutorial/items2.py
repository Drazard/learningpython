class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amtsuper().__init__(name = "GP",
                                        description="A round coin with {} stamped on the front."
                                        value=self.amt)

class Weapon(item):
    def _init__(self, name, description, value, damage):
        self.damage = damagesuper().__init(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Rock(weapon):
    def __init__(self):
        super().__init__(name="Rock",
                        description="A fist-sized rock, suitable for bludgeoning.",
                        value=0,
                        damage =5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                        description="A small dagger with some rust. at least it's better than a rock.",
                        value=10,
                        damage=10)
