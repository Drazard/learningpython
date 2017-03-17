import random
import enemies
import items

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
        print("""
        You find yourself Standing infront of a large castle door. You have heard the stories, we all have.
        Stories of other's entering and never coming out. Stories of Ghosts and Ghouls, Zombies and Giant spiders!!
        But thats all just a load of bullshit right?
        """)
        input("...")
        print("""
        but... what if it isn't? Didnt that old man down back in town say something about treasure?
        Who really knows with all that squeeking going on from his rocking chair, such a stereotypical old guy
        with his rocking chair and his pipe,
        telling people not to go near the straight-out-of-the-movies abandoned spooky castle.
        """)
        input("...")

        print("""
        well, cant hurt to have a look around for a little while. Might find something cool inside!
        """)
        input("...")

    def modify_player(self, player):
        pass

class DaggerTile(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        return"""
        This is the third room of the castle!! be careful!!

        you can see passages to the North, East, and West.
        """
    def modify_player(self, player):
        player.inventory.append(items.Dagger())
        print("Picked up {}".format(items.Dagger()))

class BoringTile(MapTile):
    def intro_text(self):
        return """
        This is a very boring part of the castle, not really a whole lot to see.
        """
class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.30:
            self.enemy = enemies.SpookySkeleton()
            self.alive_text = """
                            A Spooky Skeleton appears!
                            """

            self.dead_text = """
                            The bones of a skeleton still remain scattered accross the ground
                            """
        elif r < 0.35:
            self.enemy = enemies.BeastlyBear()
            self.alive_text = """
                            A wild Beastly Bear came running towards you
                            """

            self.dead_text = """"
                            Your new bear-skin rug looks nice in this area of the cave
                            """
        elif r < 0.65:
            self.enemy = enemies.Daniel()
            self.alive_text = """
                            You see a spider crawling around on the rocks!
                            """
            self.dead_text = """
                            There is a dead man laying here, his shirt says 'Daniel' ...Strange.
                            """
        else:
            self.enemy = enemies.GhastlyGhost()
            self.alive_text = """
                            A Ghastly Ghost swoops straight through you!
                            """
            self.dead_text = """
                            The evil spirits have long left this area of the cave
                            """

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            text = self.alive_text
        else:
            text = self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining."
            .format(self.enemy.damage, player.hp))

class TreasureTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1,50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold found!".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return"""
        Wasn't there some gold here earlier?
        """
        else:
            print("""
            You venture forward towards a large golden door. This seems interesting?
            Cautious of the dangers that could lie ahead (and despite common sense) you pull on the two massive handles.
            """)
            input("...")
            print("""
            nothing happens..
            """)
            input("...")

class LootTile(MapTile):
    def __init__(self,x ,y):
        self.loot_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.loot_claimed:
            self.loot_claimed = True
            player.inventory.append(items.VampSword())
            print("Picked up {}".format(items.VampSword()))
            player.hp -= 10

    def intro_text(self):
        if self.loot_claimed:
            return"""
            "SCREEEEECH"


            that doesnt sound good, perhaps you should leave this area.
            """
        else:
            print("""
            You stumble into what looks to be a very gothic setting. The chains hanging above cause you some concern,
            There are giant steel rings attatched to those chains! it would only take one link to break and... game over!
            As you continue you are intreiged by what is ahead, something shiny! Treasure perhaps??
            Being over-excited you trip and fall flat on your face.. (-3hp)

            ...
            """)
            input("...")
            print("""
            as you stumble to your feet it is unclear what made you fall. But what is clear is the sudden sharp pain you feel in your legs.
            This pain is unbearable, you can feel a sword-like blade pierce through your skin as if it is injecting poision into your blood stream
            You collapse once more in a wild fit, What is wrong with you? Are you going to be OK? (-7hp)

            ...
            """)
            input("...")
            print("""
            As quickly as the horrific pain had sucome your body to a seizure-like state the pain vanishes almost completely.
            Hessitent to get back on your feet again you notice the culprit of your recent missfortun: a short sword.
            A very strange sword consisting of the most perfect obsidian black hilt almost as if to imply that this sword has never been used.

            The blade is covered with a dry and crusted layer of blood over an otherwise perfectly sharpened blade.
            Wait a minute, didn't you cut yourself with this? Most interesting...
            Less interesting but possibly just as important: an etching that appears to be the shape of a small bird, or a bat perhaps?
              """)
            input("...")







class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer It's sunlight!

        Victory is yours!
        """

# This is the layout of our world map.
world_dsl = """
|EN|LT|  |  |  |  |  |  |  |  |  |  |  |  |
|BT|  |EN|  |  |  |  |  |  |  |  |  |  |  |
|BT|  |EN|  |BT|  |EN|  |  |  |  |  |  |  |
|BT|EN|DT|EN|EN|EN|BT|  |TT|  |  |  |  |  |
|TT|  |BT|  |BT|  |EN|  |BT|  |  |  |  |  |
|  |  |ST|  |  |  |EN|  |BT|  |  |  |  |  |
|  |  |  |  |  |EN|EN|EN|BT|  |VT|  |  |  |
|  |  |  |TT|EN|BT|  |  |BT|BT|EN|BT|  |  |
|  |  |  |  |  |EN|EN|BT|  |EN|  |EN|  |  |
|  |  |  |  |  |  |  |EN|EN|BT|EN|EN|  |  |
|  |  |  |  |  |  |  |  |  |BT|  |  |  |  |
|  |  |  |  |  |  |  |  |  |EN|  |  |  |  |
|  |  |  |  |  |  |  |  |  |TT|  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
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
                    "TT": TreasureTile,
                    "LT": LootTile,
                    "BT": BoringTile,
                    "DT": DaggerTile,
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
