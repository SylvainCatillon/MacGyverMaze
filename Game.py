from Map import *
from Display import *


class Game:
    """The current game"""

    def __init__(self):
        self.map = Map()
        self.display = Display(self.map)

    def choose_map(self, map_name):
        self.map.choose_map(map_name)

    def play(self):
        self.display.choose_language("english")  # add input
        self.display.say_welcome()
        self.choose_map("facile")  # add input
        while self.map.current_position != self.map.end:
            self.display.display_map()
            inp = ""
            while inp not in self.map.get_available_directions():
                inp = input("Choose a direction: {}".format(self.map.get_available_directions())).upper()
                if inp == "Q":
                    break
            if inp == "Q":
                break
            self.map.set_current_position(inp)
        if self.map.current_position == self.map.end:
            print(self.display.congrats)
        print(self.display.end)
