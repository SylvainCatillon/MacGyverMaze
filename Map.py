class Map:
    """The map of the game"""

    def __init__(self, squares, width, height):
        self.squares = squares
        self.width = width
        self.height = height
        self.squares_dict = {}
        for i in range(1, height+1):
            self.squares_dict[i] = [square for square in squares if square.y == i]




class Square:
    """Square of map"""

    def __init__(self, x, y, is_wall):
        self.x = x
        self.y = y
        self.is_wall = is_wall
