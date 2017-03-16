import random
import enemies

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


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
            self.alive_text = "A Spooky Skeleton appears!"
            self.dead_text = "The bones of a skeleton still remain scattered accross the ground"
        elif r < 0.80:
            self.enemy = enemies.BeastlyBear()
        elif r < 0.95:
            self.enemy = enemies.Daniel()
        else:
            self.enemy = enemies.GhastlyGhost()

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text if self.enemy.is_alive() else self.dead_text
            return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".
                    format(self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer It's sunlight!

        Victory is yours!
        """

        def modify_player(self, player):
            if self.enemy.is_alive():
                player.hp = player.hp - self.enemy.damage
                print("Enemy does {} damage, you have {} HP remaining.".
                    format(self.enemy.damage, player.hp))
world_map = [
    [None,VictoryTile(1,0),None],
    [None,EnemyTile(1,1),None],
    [EnemyTile(0,2),StartTile(1,2),EnemyTile(2,2)],
    [None,EnemyTile(1,3),None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
        try:
            return world_map[y][x]
        except IndexError:
            return None

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.title_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))
