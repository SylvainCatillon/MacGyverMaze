from Map import *
from Display import *


class Game:
    """The current game"""

    def __init__(self):
        self.map = Map()
        self.map.choose_map("facile")  # add input
        self.display = Display("english", self.map)  # add input

    def choose_map(self):
        self.map.choose_map("facile")  # add input

    def play(self):
        while self.map.current_position != self.map.end:
            self.display.display_map()
            inp = ""
            while inp not in self.map.get_available_directions():
                inp = input("Choose a direction: {}".format(self.map.get_available_directions())).upper()
                print(inp)
                if inp == "Q":
                    break
            if inp == "Q":
                break
            self.map.set_current_position(inp)
        if self.map.current_position == self.map.end:
            print(self.display.congrats)
        print(self.display.end)
