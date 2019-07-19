class Map:
    """Get the Map from a .txt file, stocking the squares as a list (y indices) of lists (x indices).
    maps must be squares
    .txt legend: 0 == clear, 1 == wall, S == start, K == keeper"""

    SYMBOL_DICT = {
        "floor": "F",
        "wall": "W",
        "start": "S",
        "keeper": "K"}

    def __init__(self):
        self.wall_list = []
        self.floor_list = []
        self.start = (0, 0)
        self.keeper = (0, 0)
        self.height = 1
        self.width = 1

    @property
    def available_floor_list(self):
        return [cords for cords in self.floor_list if
                cords != self.start and cords != self.keeper]

    def load_map(self, map_name):
        """Read the map file.
         Fill floor_list and wall_list.
         Set start position, keeper position, height and width of the map"""
        with open(map_name + ".txt", "r") as file:
            string = file.read()
        y_list = string.split("\n")
        height = len(y_list)
        self.height = height
        width = 0
        x = 0
        for y, e in enumerate(y_list):
            for x, f in enumerate(e): # Raise error si map pas valide???
                f = f.upper()
                if f in self.SYMBOL_DICT.values():
                    if f == self.SYMBOL_DICT["wall"]:
                        self.wall_list.append((x, y))
                    else:
                        self.floor_list.append((x, y))
                        if f == self.SYMBOL_DICT["start"]:
                            self.start = (x, y)
                        elif f == self.SYMBOL_DICT["keeper"]:
                            self.keeper = (x, y)
            if x >= width:
                width = x+1
        self.width = width
