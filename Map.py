
class Map:
    """The map of the game"""

    def __init__(self, map_name):
        """Get the Map from a .txt file, stocking the squares as a list (y indexes) of lists (x indexes)
        .txt legend: 0 == clear, 1 == wall, S == stars, E == end"""
        file_name = map_name + ".txt"
        squares_list = []
        with open(file_name, "r") as file:
            string = file.read()
            y_list = string.split("\n")
            height = len(y_list)
            for i in range(height-1, -1, -1):  # Run backwards trough y_list
                x_list = []
                for j, e in enumerate(y_list[i]):
                    if e == "S":
                        self.start = (j+1, height-i)  # Create a tuple with (x,y). Height-i because running backwards
                    elif e == "E":
                        self.end = (j+1, height-i)  # Create a tuple with (x,y). Height-i because running backwards
                    x_list.append(e)
                squares_list.append(x_list)
        self.squares_list = squares_list
        self.height = height
        self.width = len(squares_list[0])
        self.current_position = self.start
        self.directions = ["N", "E", "S", "W"]

    @property
    def current_north(self):
        return (self.current_position[0], self.current_position[1]+1)

    @property
    def current_east(self):
        return (self.current_position[0] + 1, self.current_position[1])

    @property
    def current_south(self):
        return (self.current_position[0], self.current_position[1] - 1)

    @property
    def current_west(self):
        return (self.current_position[0] - 1, self.current_position[1])

    @staticmethod
    def coord_to_index(n):
        return n-1

    @staticmethod
    def index_to_coord(n):
        return n+1


    def set_current_position(self, direction):
        if direction == "N":
            self.current_position = self.current_north
        if direction == "E":
            self.current_position = self.current_east
        if direction == "S":
            self.current_position = self.current_south
        if direction == "W":
            self.current_position = self.current_west

    def get_square(self,x, y):
        """Return the status of the square"""
        return self.squares_list[self.coord_to_index(y)][self.coord_to_index(x)]

    def is_wall(self, x, y):
        """Return true if there is a wall on the square"""
        return self.get_square(x, y) == "1"

    """def get_available_directions(self):
        x = self.current_position[0]
        y = self.current_position[1]
        available_directions = []
        if self.is_wall()"""




"""map = Map("facile")
print(map.get_square(3, 6))
print(map.is_wall(3, 6))
print(map.is_wall(2, 15))
print(map.height)
print(map.width)
print(map.start)
print(map.end)"""
