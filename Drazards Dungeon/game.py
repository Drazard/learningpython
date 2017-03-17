from player import Player
import world
from collections import OrderedDict
import os
import time


def play():
    clear = lambda: os.system('cls')
    clear()
    print("""
    ====  Drazards Dungeon  ====
    """)
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("Your journey has come to an early end!")

def get_avalible_actions(room, player):
    actions = OrderedDict()
    print ("\n\nYour options: \n")
    action_adder(actions, 'c', player.print_info, "Character Info")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")
        if player.hp < 100:
            action_adder(actions, 'h', player.heal, "Heal")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, 'n', player.move_north, "Go north")
        if world.tile_at(room.x, room.y +1):
            action_adder(actions, 's', player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "Go west")
    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print(" {} = {}".format(name, hotkey))

def choose_action(room, player):
    action = None
    while not action:
        avalible_actions = get_avalible_actions(room, player)
        action_input = input("\n Action: ")
        action = avalible_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")

play()
