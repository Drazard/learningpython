from player import Player
import world

def play():
    print("Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        a_input = get_player_command()
        if a_input in ['n', 'N']:
            player.move_north()
        elif a_input in ['s', 'S']:
            player.move_south()
        elif a_input in ['e', 'E']:
            player.move_east()
        elif a_input in ['w', 'W']:
            player.move_west()
        elif a_input in ['i', 'I']:
            player.print_inventory()
        elif a_input in ['a', 'A']:
            player.attack()
        else:
            print("Invalid action!!")


def get_player_command():
    return input('Action: ')


play()
