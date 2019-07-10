class Item:

    def __init__(self, name):  # arg cords and position maybe useless
        self.cords = (0, 0)
        self.name = name
        self.symbol = name[0].upper()
        self.found = False
