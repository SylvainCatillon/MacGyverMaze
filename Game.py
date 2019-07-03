from Map import *
from Display import *


def init_game():
    current_map = Map()
    current_map.choose_map("facile")  # add input when several maps
    return current_map


def play(current_map):
    while current_map.current_position != current_map.end:
        display_map(current_map)
        inp = ""
        while inp not in current_map.get_available_directions():
            inp = input("Choose a direction: {}".format(current_map.get_available_directions())).upper()
            if inp == "Q":
                print("Thank you for playing")
                break
        current_map.set_current_position(inp)
    if current_map.current_position == current_map.end:
        print("Congratulations, you reached the exit!!!")


play(init_game())
