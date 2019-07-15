from random import randrange


class Map:
    """Get the Map from a .txt file, stocking the squares as a list (y indexes) of lists (x indexes).
    maps must be squares
    .txt legend: 0 == clear, 1 == wall, S == start, K == keeper"""

    SYMBOL_DICT = {
        "floor": "F",
        "wall": "W",
        "start": "S",
        "keeper": "K"}

    def __init__(self):
        self.squares_dict = {}
        self.start = (0, 0)
        self.keeper = (0, 0)
        self.height = 1
        self.width = 1

    def load_map(self, map_name):
        """Read the map file, stocking squares in dict (keys == (x, y)), and set start, end, height and width"""
        with open(map_name + ".txt", "r") as file:
            string = file.read()
            y_list = string.split("\n")
            height = len(y_list)
            self.height = height
            width = 0
            for y, e in enumerate(y_list):
                for x, f in enumerate(e): # Raise error si map pas valide???
                    f = f.upper()
                    if f in self.SYMBOL_DICT.values():
                        self.squares_dict[(x, y)] = f
                        if f == self.SYMBOL_DICT["start"]:
                            self.start = (x, y)
                            self.squares_dict[(x, y)] = self.SYMBOL_DICT["floor"]
                        elif f == self.SYMBOL_DICT["keeper"]:
                            self.keeper = (x, y)
                if x >= width:
                    width = x+1
        self.width = width

    def place_items(self, items_dict):
        """Place randomly the items on the map
        Take a dict of items,and give random cords to each item"""
        floor_list = [key for key, value in self.squares_dict.items()
                      if key != self.start and key != self.keeper and value != self.SYMBOL_DICT["wall"]]
        for item in items_dict.values():
            cords = floor_list.pop(randrange(len(floor_list)))
            item.cords = cords
            self.squares_dict[cords] = item.symbol

    def get_square(self, cords): # rename en get_symbol
        """Return the status of the square"""
        return self.squares_dict[cords]

    def is_wall(self, cords):
        """Return true if there is a wall on the square"""
        return self.get_square(cords) == self.SYMBOL_DICT["wall"]

    def good_square(self, cords):
        """Return True if the square is good(is on the map and is not a wall)"""
        return cords in self.squares_dict and not self.is_wall(cords)


