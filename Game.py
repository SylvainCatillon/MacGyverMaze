from random import randrange
from Map import Map
from Item import Item
from Player import Player
# from Terminal.Display import Display
# from Terminal.Input import Input
from PyGame.Display import Display
from PyGame.Input import Input


class Game:
    """The current game"""

    ITEM_NAMES_LIST = ["Needle", "Tube", "Ether"]

    def __init__(self):
        self.keep_playing = True
        self.player = Player()
        self.items_list = [Item(name) for name in self.ITEM_NAMES_LIST]
        self.map = Map()
        self.map.load_map("maps/facile")
        self.input = Input()
        self.display = Display(
            self.map.width, self.map.height,
            self.map.floor_list, self.map.wall_list)

    def place_items(self):
        """Place randomly the items on the map"""
        square_list = self.map.available_floor_list
        for item in self.items_list:
            cords = square_list.pop(randrange(len(square_list)))
            item.cords = cords

    def get_new_cords(self):
        """Get the new cords of the player.
        Ask an input direction, quit if the direction is "Q".
        Else, convert direction into cords by asking Player.
        Return the cords if they are on the map and are not a wall."""
        direction = self.input.game_input
        if direction == "Q":
            return "QUIT"
        cords = self.player.directions_dict()[direction]
        if cords not in self.map.floor_list:
            return self.get_new_cords()
        return cords

    def check_items(self):
        """Check if the player found an item"""
        cords = self.player.cords
        for item in self.items_list:
            if not item.found and cords == item.cords:
                item.found = True
                self.display.item_collected(item.name, cords)

    def reset_game(self):
        """Reset some value to prepare a new game"""
        for item in self.items_list:
            item.found = False
        self.display.reset()

    def end(self):
        """Check if the game is over. Return False if the game continue.
        Return true and calculate victory if the game is ending"""
        if self.player.cords != self.map.keeper:
            return False
        victory = True
        for item in self.items_list:
            if not item.found:
                victory = False
        self.display.end(victory)
        self.keep_playing = self.input.end_input
        if self.keep_playing:
            self.reset_game()
        return True

    def play(self):
        """Play the Game"""
        new_cords = self.get_new_cords()
        if new_cords == "QUIT":
            self.keep_playing = False
        else:
            self.player.cords = new_cords
            self.display.move_player(new_cords)
            self.check_items()
            if not self.end():
                return self.play()

    def launch(self):
        """Launch the game"""
        self.player.cords = self.map.start
        self.place_items()
        self.display.start(self.items_list, self.map.start, self.map.keeper)
        self.play()
