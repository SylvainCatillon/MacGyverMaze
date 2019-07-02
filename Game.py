from Map import *


def init_game():
    map = Map("facile")
    print("You are at {}".format(map.current_position))
    return map


def play(map):
    while map.current_position != map.end:
        inp = input("Choose a direction: {}".format(map.get_available_directions()))
        if inp.lower() == "q":
            print("Merci d'avoir joué")
            break
        elif inp.upper() not in map.get_available_directions():
            print("Wrong input")
            return play(map)
        print(inp)
        map.set_current_position(inp.upper())
        print("You are at {}".format(map.current_position))
    if map.current_position == map.end:
        print("Bravo, vous avez atteint la sortie!!!")


current_map = init_game()
play(current_map)