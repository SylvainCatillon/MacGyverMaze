from Map import *
from Display import *
from PyGame import *


class Game:
    """The current game"""

    ITEM_NAMES_LIST = ["needle", "tube", "ether"]

    def __init__(self):
        self.map = Map()
        self.display = GameDisplay(self.map)
        self.search_dict = {}
        self.found_list = []

    def choose_map(self, map_name):
        self.map.choose_map(map_name)

    def play(self):
        #self.display.choose_language("english")  # add input
        #self.display.welcome()
        self.choose_map("facile")  # add input
        self.display.start()
        self.search_dict = self.map.place_items(self.ITEM_NAMES_LIST)
        while not self.end():
            inp = ""
            while inp not in self.map.get_available_directions():
                inp = input("Choose a direction: {}".format(self.map.get_available_directions())).upper()
                if inp == "Q":
                    break
                inp = self.temp_pave_num(inp)
            if inp == "Q":
                break
            self.map.set_current_position(inp)
            self.check_items()
        #self.display.end()

    def check_items(self):
        """Check if the player found an item"""
        cords = self.map.current_position
        if cords in self.search_dict:
            item = self.search_dict.pop(cords)
            self.display.item_collected(item.name)
            self.found_list.append(item.name)
            self.map.squares_dict[cords] = Map.CLEAR_SQUARE

    def end(self):
        """Check if the game is over. Return False if the game continue.
        Return true and calculate victory if the game is ending"""
        if self.map.current_position != self.map.keeper:
            return False
        victory = True
        for name in self.ITEM_NAMES_LIST:  # Replace by len(found_list) == len(ITEM_NAMES)??
            if name not in self.found_list:
                victory = False
        #if victory:
            #self.display.congrats()
        #else:
            #self.display.death()
        return True

    @staticmethod
    def temp_pave_num(inp):
        return inp.replace("4", "W").replace("8", "N").replace("2", "S").replace("6", "E")
