from Map import *
from Item import *
from Display import *
import Player
from Pygame.PyGame import *


class Game:
    """The current game"""

    ITEM_NAMES_LIST = ["Needle", "Tube", "Ether"]
    DISPLAY_CLASS = Display

    def __init__(self):
        self.map = Map()
        self.player = Player.Player()
        self.display = self.DISPLAY_CLASS(self)
        self.items_dict = {}

    def init_map(self):
        """Initialize the map, by choosing a map and placing items and player on it"""
        self.map.choose_map("facile")  # add input?
        self.player.cords = self.map.start
        for name in self.ITEM_NAMES_LIST:
            item = Item(name)
            self.items_dict[item.symbol] = item  # Create a dict with item symbol as key and Item object as value
        self.map.place_items(self.items_dict)

    def get_new_cords(self):
        """Get the new cords of the player.
        Ask a input direction, quit if the direction is "Q". Else, convert direction into cords by asking Player.
        Verify that the new cords are on the map and are not a wall, and then return the cords"""
        direction = self.temp_input()
        if direction == "Q":
            return "QUIT"
        # add raise error if direction not in ["UP", "RIGHT", "LEFT", "DOWN"]? Ou inutile parce-que déjà check dans input?
        cords = self.player.directions_dict()[direction]
        if not self.map.good_square(cords):
            return self.get_new_cords()
        return cords

    def play(self):
        """Play the Game"""
        self.init_map()
        self.display.start()
        while not self.end():
            new_cords = self.get_new_cords()
            if new_cords == "QUIT":
                break
            self.player.cords = new_cords
            self.display.move_player()
            self.check_items()

    def check_items(self):
        """Check if the player found an item"""
        cords = self.player.cords
        symbol = self.map.get_square(cords)
        if symbol in self.items_dict:
            item = self.items_dict[symbol]
            item.found = True
            self.display.item_collected(item.name)
            self.map.squares_dict[cords] = Map.CLEAR_SQUARE

    """
    Possibilité de fonction avec une liste d'items plutot qu'un dict:
    def check_items(self):
        cords = self.player.cords
        for item in self.items_list:
            if not item.found and item.cords == cords:
                item.found = True
                self.display.item_collected(item.name)
                self.map.squares_dict[cords] = Map.CLEAR_SQUARE"""

    def end(self):
        """Check if the game is over. Return False if the game continue.
        Return true and calculate victory if the game is ending"""
        if self.player.cords != self.map.keeper:
            return False
        victory = True
        for item in self.items_dict.values():
            if not item.found:
                victory = False  # Renplacer par compteur?
        self.display.end(victory)
        return True

    @staticmethod
    def temp_pave_num(inp):
        """Temporary method to convert input into direction"""
        return inp.replace("4", "LEFT").replace("8", "UP").replace("2", "DOWN").replace("6", "RIGHT")

    @staticmethod
    def temp_input():
        """Temporary method to get input"""
        inp = ""
        while inp not in ["DOWN", "RIGHT", "UP", "LEFT"]:
            inp = input("Choose a direction").upper()
            if inp == "Q":
                break
            inp = Game.temp_pave_num(inp)
        return inp
