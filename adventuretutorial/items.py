class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class rock(Weapon):
    def __init__(self):
        self.name = "rock"
        self.description = "A fist sized rock, suitable for bludgeoning."
        self.damage = 5


class Dagger(Weapon):
    def __init__(self):
        self.name ="Dagger"
        self.description = "A small dagger with some rust. " \
                            "Somewhat more dangerous than a rock."
        self.damage = 10


class RustySword(Weapon):
    def _init(self):
        self.name = "Rusty sword"
        self.description = "this word is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self. healing_value = 10
