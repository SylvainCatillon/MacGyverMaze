from Item import *
from random import *


class Map:
    """Get the Map from a .txt file, stocking the squares as a list (y indexes) of lists (x indexes).
    maps must be squares
    .txt legend: 0 == clear, 1 == wall, S == start, K == keeper"""

    CLEAR_SQUARE = "0"
    WALL = "1"
    START = "S"
    KEEPER = "K"

    def __init__(self):
        self.squares_dict = {}
        self.start = (0, 0)
        self.keeper = (0, 0)
        self.height = 15
        self.width = 15
        self.current_position = self.start

    @property
    def current_north(self):
        if self.current_position[1] == self.height:
            return None
        return self.current_position[0], self.current_position[1] - 1

    @property
    def current_east(self):
        if self.current_position[0] == self.width:
            return None
        return self.current_position[0] + 1, self.current_position[1]

    @property
    def current_south(self):
        if self.current_position[1] == 0:
            return None
        return self.current_position[0], self.current_position[1] + 1

    @property
    def current_west(self):
        if self.current_position[0] == 0:
            return None
        return self.current_position[0] - 1, self.current_position[1]

    @property
    def directions_dict(self):
        return {"N": self.current_north, "E": self.current_east, "S": self.current_south, "W": self.current_west}

    def choose_map(self, map_name):
        """Read the map file, stocking squares in dict (keys == (x, y)), and set start, end, height and width"""
        file_name = map_name + ".txt"
        with open(file_name, "r") as file:
            string = file.read()
            y_list = string.split("\n")
            height = len(y_list)
            self.height = height
            y = -1
            for e in y_list:
                y += 1
                x = -1
                for f in e:
                    x += 1
                    self.squares_dict[(x, y)] = f
                    if f == self.START:
                        self.start = (x, y)
                    elif f == self.KEEPER:
                        self.keeper = (x, y)
        self.width = x + 1  # length == last index + 1
        self.current_position = self.start

    def place_items(self, names_list):
        """Place randomly the items on the map
        Take a list of items names, return a dict of items, with cords (x, y) as key, and Object Item as value"""
        items_dict = {}
        floor_list = [key for key, value in self.squares_dict.items()
                      if key != self.start and key != self.keeper and value != self.WALL]
        for item_name in names_list:
            cords = floor_list.pop(randrange(len(floor_list)))
            items_dict[cords] = Item(item_name, cords)
            self.squares_dict[cords] = item_name[0].upper()
        return items_dict

    """
    OLD METHOD WITH CHOICE/REMOVE INSTEAD OF RANDRANGE/POP
    def place_items(self, names_list):
        items_dict = {}
        floor_list = [key for key, value in self.squares_dict.items()
                      if key != self.start and key != self.keeper and value != self.WALL]
        for item_name in names_list:
            cords = choice(floor_list)
            items_dict[cords] = Item(item_name, cords)
            self.squares_dict[cords] = item_name[0].upper()
            floor_list.remove(cords)
        return items_dict"""

    def set_current_position(self, chosen_direction):
        """Take the direction chosen by the player ("N", "E", "S" or "W"), and set his position"""
        # To do: add raise error if chosen_direction not in get_available_directions()
        if chosen_direction == "N":
            self.current_position = self.current_north
        if chosen_direction == "E":
            self.current_position = self.current_east
        if chosen_direction == "S":
            self.current_position = self.current_south
        if chosen_direction == "W":
            self.current_position = self.current_west

    def get_square(self, cords):
        """Return the status of the square"""
        if cords == self.current_position:
            return "P"
        return self.squares_dict[cords]

    def is_wall(self, cords):
        """Return true if there is a wall on the square"""
        return self.get_square(cords) == self.WALL

    def get_available_directions(self):
        """Return a list of the current available directions"""
        available_directions = []
        for key in self.directions_dict:
            direction = self.directions_dict[key]
            if direction is not None and not self.is_wall(direction):
                available_directions.append(key)
        return available_directions
