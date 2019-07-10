from Map import *
from Item import *
from Display import *
from Pygame.PyGame import *


class Game:
    """The current game"""

    ITEM_NAMES_LIST = ["needle", "tube", "ether"]

    def __init__(self):
        self.map = Map()
        self.display = Display(self.map)
        #  self.display = GameDisplay(self.map)
        self.items_dict = {}

    def init_map(self):
        """Initialize the map, by choosing a map and placing items on it"""
        self.map.choose_map("facile")
        for name in self.ITEM_NAMES_LIST:
            item = Item(name)
            self.items_dict[item.symbol] = item
        self.map.place_items(self.items_dict)

    def play(self):
        """Play the Game"""
        self.init_map()
        self.display.choose_language("english")  # add input
        self.display.welcome()
        #self.choose_map("facile")  # add input
        #self.display.start()
        #self.search_dict = self.map.place_items(self.ITEM_NAMES_LIST)
        while not self.end():
            self.display.display_map()
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
        self.display.end()

    def check_items(self):
        """Check if the player found an item"""
        cords = self.map.current_position
        symbol = self.map.get_square(cords)
        if symbol in self.items_dict:
            self.items_dict[symbol].found = True
            self.map.squares_dict[cords] = Map.CLEAR_SQUARE

    def end(self):
        """Check if the game is over. Return False if the game continue.
        Return true and calculate victory if the game is ending"""
        print(self.map.current_position)
        if self.map.current_position != self.map.keeper:
            return False
        victory = True
        for item in self.items_dict.values():
            if not item.found:
                victory = False  # Renplacer par compteur?
        print(victory)
        """if victory: victory(). else: game_over()"""
        return True

    @staticmethod
    def temp_pave_num(inp):
        return inp.replace("4", "W").replace("8", "N").replace("2", "S").replace("6", "E")
