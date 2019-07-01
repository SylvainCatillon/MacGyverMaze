from Map import *

def init_game():
    map = Map("facile")
    print("You are at {}".format(map.current_position))
    return map


def play(map):
    while map.current_position != map.end:
        inp = input("Choose a direction: {}".format(map.get_available_directions()))
        if inp.lower() == "q":
            break
        elif inp.upper() not in map.get_available_directions():
            print("Wrong input")
            return play(map)
        print(inp)
        map.set_current_position(inp.upper())
        print("You are at {}".format(map.current_position))

map = init_game()
play(map)
print("Bravo!")