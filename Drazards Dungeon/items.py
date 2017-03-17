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
        self.value = 1
        self.heal = 0


class Dagger(Weapon):
    def __init__(self):
        self.name ="Dagger"
        self.description = "A small dagger with some rust. " \
                            "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 30
        self.heal = 0


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty sword"
        self.description = "this word is showing its age, " \
                            "but still has some fight in it."
        self.damage = 20
        self.value = 100
        self.heal = 0

class VampSword(Weapon):
    def __init__(self):
        self.name = "Vampiric Sword"
        self.description = "A sword of strange power"
        self.damage = 40
        self.heal = 5
        self.pickup = """
                        What a strange sword indeed. The hilt is obsidion black, a perfect mirror polish
                        almost as if to imply that this sword has never been used.

                        Yet underneath the dry and crusted layer of blood covering most of the perfectly sharp edge of the blade
                        there lies a marking that makes the shape of a small bird, or a bat perhaps?
                        """

class BattleAxe(Weapon):
    def __init__(self):
        self.name = "Battle Axe"
        self.description = " An old axe."
        self.heal = self.heal = 0




class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self. healing_value = 10
        self.value = 13
