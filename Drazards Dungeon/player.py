import items
import world
import random

class Player:
    def __init__(self):
        self.inventory = [items.rock(),
                            items.CrustyBread()]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 5
        self.victory = False
        self.teleport = True
        self.damage = self.damage()

    def is_alive(self):
        return self.hp > 0

    def print_info(self):
        best_weapon = self.most_powerful_weapon()
        print("\n Current health: {}\n Current weapon: {}".format(self.hp, best_weapon))

    def print_inventory(self):
        print("\n\nInventory:\n")
        for item in self.inventory:
            print('*' + str(item))
        print("Gold: {}".format(self.gold))
        best_weapon = self.most_powerful_weapon()

    def heal(self):
        consumables = [item for item in self.inventory
                        if isinstance(item, items.Consumable)]
        if not consumables:
            print("\n\nYou do not have any items to heal you\n")
            return

        for i, item in enumerate(consumables, 1):
            print("\n\nChoose an item to use as heal: \n")
            print("{}. {}".format(i, item))
            valid = False
            while not valid:
                choice = input("")
                try:
                    to_eat = consumables[int(choice) - 1]
                    self.hp = min(100, self.hp + to_eat.healing_value)
                    self.inventory.remove(to_eat)
                    print("\n\nYou ate {} Current HP: {}\n".format(to_eat, self.hp))
                    valid = True
                except (ValueError, IndexError):
                    print("\nInvalid choice, try again.\n")

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        enemy.hp -= self.damage
        print("\n\nYou use {} against {}!\nYou delt {} damage.".format(best_weapon.name, enemy.name, self.damage))
        if not enemy.is_alive():
            print("you killed {}!\n".format(enemy.name))
            print("Your HP is: {}\n".format(self.hp))
        else:
            try:
                if best_weapon.heal != None:
                    self.hp = min(100, self.hp + best_weapon.heal)
                    print("Healed: {}\n".format(best_weapon.heal))
            except AttributeError:
                pass

            print("{} delt {} Damage.\n Enemy has {} HP remaining.".format(enemy.name, enemy.damage, enemy.hp))
            self.hp = self.hp - enemy.damage
            print("You have {} HP remaining."
            .format(self.hp))

    def damage(self):
        best_weapon = self.most_powerful_weapon()
        r = random.randint(1,10)
        best_weapon.damage -= r
        return best_weapon.damage

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move (dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)
