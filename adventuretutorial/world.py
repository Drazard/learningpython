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
        if r < 0.10:
            self.enemy = enemies.SpookySkeleton()
            self.alive_text = "A Spooky Skeleton appears!"
            self.dead_text = "The bones of a skeleton still remain scattered accross the ground"
        elif r < 0.20:
            self.enemy = enemies.BeastlyBear()
            self.alive_text = "A wild Beastly Bear came running towards you"
            self.dead_text = "Your new bear-skin rug looks nice in this area of the cave"
        elif r < 0.90:
            self.enemy = enemies.Daniel()
            self.alive_text = "You see a spider crawling around on the rocks!"
            self.dead_text = "There is a dead man laying here, his shirt says 'Daniel' ...Strange."
        else:
            self.enemy = enemies.GhastlyGhost()
            self.alive_text = "A Ghastly Ghost swoops straight through you!"
            self.dead_text = "The evil spirits have long left this area of the cave"

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
    def modify_player(self, player):
        player.victory = true

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer It's sunlight!

        Victory is yours!
        """

# This is the layout of our world map.
world_dsl = """
|EN|VT|EN|
|EN|EN|EN|
|EN|ST|EN|
|EN|EN|EN|
"""

# Creating the function to test if our world map is valid.
def is_dsl_valid(dsl):
    # Checking if we have only one starting room.
    if dsl.count("|ST|") != 1:
        # If we do not have a starting room, our map is invalid.
        return False
    # Checking that there is at lesat one Victory room.
    if dsl.count("|VT|") == 0:
        # If our vicroty room doenst exist, our map is invalid.
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                    "EN": EnemyTile,
                    "ST": StartTile,
                    "  ": None}

world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    # Iterate over each line in the DSL.
    # var y is used because we are working with an X=Y grid.
    for y, dsl_row in enumerate(dsl_lines):
        # Creating an object to store the tiles
        row = []
        # Splitting the lines into abbreviations after each "|"
        dsl_cells = dsl_row.split("|")
        # the split includes the beginning and end of the line
        # so we need to remove those non-existant cells.
        dsl_cells = [c for c in dsl_cells if c]
        # Iterate over each cell in the DSL line
        for x, dsl_cell in enumerate(dsl_cells):
            # This looks up the abbreviation in the dictionary
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            # If the dict returns a valid type, create
            # a new tile object passed through the X-Y cords
            # and add it to the row object.
            #if none was found in dict add None
            row.append(tile_type(x, y) if tile_type else None)
        # Add the whole row into the world_map
        world_map.append(row)

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
