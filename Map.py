
class Map:
    """Get the Map from a .txt file, stocking the squares as a list (y indexes) of lists (x indexes)
        .txt legend: 0 == clear, 1 == wall, S == stars, E == end"""

    CLEAR_SQUARE = "0"
    WALL = "1"
    START = "S"
    END = "E"

    def __init__(self, map_name):
        self.squares_list, self.start, self.end = self.file_to_map(map_name)
        self.height = len(self.squares_list)
        self.width = len(self.squares_list[0])
        self.current_position = self.start
        self.directions = {
            "N": self.current_north, "E": self.current_east, "S": self.current_south, "W": self.current_west}

    def current_north(self):
        return (self.current_position[0], self.current_position[1]+1)

    def current_east(self):
        return (self.current_position[0] + 1, self.current_position[1])

    def current_south(self):
        return (self.current_position[0], self.current_position[1] - 1)

    def current_west(self):
        return (self.current_position[0] - 1, self.current_position[1])

    @staticmethod
    def coord_to_index(n):
        return n-1

    @staticmethod
    def index_to_coord(n):
        return n+1

    def file_to_map(self, map_name):
        """Read the map file, stocking the squares as a list (y indexes) of lists (x indexes), and set start and end"""
        file_name = map_name + ".txt"
        squares_list = []
        with open(file_name, "r") as file:
            string = file.read()
            y_list = string.split("\n")
            height = len(y_list)
            for i in range(height-1, -1, -1):  # Run backwards trough y_list
                x_list = []
                for j, e in enumerate(y_list[i]):
                    if e == self.START:
                        start = (j+1, height-i)  # Create a tuple with (x,y). Height-i because running backwards
                    elif e == self.END:
                        end = (j+1, height-i)  # Create a tuple with (x,y). Height-i because running backwards
                    x_list.append(e)
                squares_list.append(x_list)
        return squares_list, start, end

    def set_current_position(self, chosen_direction):
        """Take the direction chosen by the player, and set his position"""
        #To do: add raise error if chosen_direction not in get_available_directions()
        if chosen_direction == "N":
            self.current_position = self.current_north()
        if chosen_direction == "E":
            self.current_position = self.current_east()
        if chosen_direction == "S":
            self.current_position = self.current_south()
        if chosen_direction == "W":
            self.current_position = self.current_west()

    def get_square(self,x, y):
        """Return the status of the square"""
        return self.squares_list[self.coord_to_index(y)][self.coord_to_index(x)]

    def is_wall(self, coord):
        """Return true if there is a wall on the square"""
        return self.get_square(coord[0], coord[1]) == self.WALL

    def get_available_directions(self):
        """Return a list of the current available directions"""
        available_directions = []
        for key in self.directions:
            if not self.is_wall(self.directions[key]()):
                available_directions.append(key)
        return available_directions


"""map = Map("facile")
print(map.get_square(3, 6))
print(map.is_wall(3, 6))
print(map.is_wall(2, 15))
print(map.height)
print(map.width)
print(map.start)
print(map.end)"""
