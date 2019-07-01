from Map import *


def play():
    map = Map("facile")
    while map.current_position != map.end:
        inp = input("Choose a direction: N, E, S, W")
        if inp.lower() == "q":
            break
        elif inp.upper() not in map.directions:
            print("Wrong input")
            return play()
        print(inp)
        map.set_current_position(inp.upper())
        print("You are at {}".format(map.current_position))

play()
print("Bravo!")