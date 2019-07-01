
class Map:
    """The map of the game"""

    def __init__(self, map_name):
        file_name = map_name + ".txt"
        squares_list = []
        with open(file_name, "r") as file:
            string = file.read()
            y_list = string.split("\n")
            for i in range(len(y_list)-1,-1,-1):
                squares_list.append([e for e in y_list[i]])
        self.squares_list = squares_list
        self.height = len(squares_list)
        self.width = len(squares_list[0])

    def get_square(self,x, y):
        """Return the value of the square"""
        return self.squares_list[y-1][x-1]

    def is_wall(self, x, y):
        """Return true if there is a wall on the square"""
        return self.get_square(x, y) == "1"


map = Map("facile")
print(map.get_square(3, 6))
print(map.is_wall(3, 6))
print(map.is_wall(2, 15))
print(map.height)
print(map.width)
