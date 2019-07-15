class Item:

    def __init__(self, name):
        self.cords = (0, 0)
        self.name = name
        self.symbol = name[0].upper()
        self.found = False
