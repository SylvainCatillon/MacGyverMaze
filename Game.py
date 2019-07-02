from Map import *


def init_game():
    map = Map("facile")
    print("Welcome in the game! You are at position {}".format(map.current_position))
    return map


def play(map):
    while map.current_position != map.end:
        inp = input("Choose a direction: {}".format(map.get_available_directions()))
        if inp.lower() == "q":
            print("Thank you for playing")
            break
        elif inp.upper() not in map.get_available_directions():
            print("Wrong input")
            return play(map)
        print(inp)
        map.set_current_position(inp.upper())
        print("You are at {}".format(map.current_position))
    if map.current_position == map.end:
        print("Congratulations, you reached the exit!!!")


current_map = init_game()
play(current_map)