import items, enemies

class Maptile:
    def __init__(self, x, x):
        self.x = # XXX:
        self.y = y

def intro_text(self):
    raise NotImplementedError()

def modify_player(self, player):
    raise NotImplementedError()

class Startingroom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and forboding.
        """

        def modify_player(self, player)
        #Room has no action on player
        pass

class LootRoom(Maptile):
    def self __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self.item)
    self.add_loot(player)

class Enemyroom(MapTle):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. you have {} HP remaining.".format(self.enemy.damage, the_player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. you must forge onwards.
        """

    def modify_player(self, player):
        #room has no action on player
        pass

class SpookySkeletonRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.SpookySkeleton())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A spooky skeleton rises up from its grave in front of you!
            """
        else:
            return """
            The bones of a SpookySkeleton remain scattered accross the caves floor.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x ,y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return """
        You notice something shiny in the corner.
        It's a dagger! you pick it up.
        """
