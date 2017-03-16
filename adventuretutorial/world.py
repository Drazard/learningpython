import items, world, random

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very boring part of the cave.
        """
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.SpookySkeleton()
        elif r < 0.80:
            self.enemy = enemies.BeastlyBear()
        elif r < 0.95:
            self.enemy = enemies.Daniel()
        else:
            self.enemy = enemies.GhastlyGhost()

        super().__init__(x, y)

        def intro_text(self):
            if self.enemy.is_alive():
                return "A {} awaits!".format(self.enemy.name)
            else:
                return "you have defeated the {}".format(self.enemy.name)


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer It's sunlight!


        Victory is yours!
        """

world_map = [
    [None,VictoryTile(1,0),None],
    [BoringTile(0,2),StartTile(1,2),EnemyTile(2,2)],
    [None,BoringTile(1,3),None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
