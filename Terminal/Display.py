from config import display_config as cfg


class Display:
    """Class in charge of the display"""

    def __init__(self, map_width, map_height, floor_list, wall_list):
        self.map_width = map_width
        self.map_height = map_height
        self.floor_list = floor_list
        self.wall_list = wall_list
        self.keeper_pos = (0, 0)
        self.item_dict = {}

    def welcome(self):
        print(cfg["welcome_text"].format(len(self.item_dict)))

    @staticmethod
    def end(victory):
        if victory:
            print(cfg["victory_text"])
        else:
            print(cfg["defeat_text"])
        print(cfg["end_text"])

    def item_collected(self, item_name, cords):
        print(cfg["item_collected"] + item_name)
        del self.item_dict[cords]
        self.display_map(cords)

    def display_map(self, player_cords):
        display_string = ""
        for y in range(self.map_height):
            for x in range(self.map_width):
                cords = (x, y)
                if cords in self.item_dict:
                    display_string += self.item_dict[cords]
                elif cords == player_cords:
                    display_string += "P"
                elif cords == self.keeper_pos:
                    display_string += "K"
                elif cords in self.floor_list:
                    display_string += " "
                elif cords in self.wall_list:
                    display_string += "|"
                else:
                    display_string += "0"
            display_string += "\n"
        print(display_string)

    def start(self, items_list, start, keeper):
        self.keeper_pos = keeper
        for item in items_list:
            self.item_dict[item.cords] = item.name[0].upper()
        self.welcome()
        self.display_map(start)

    def move_player(self, cords):
        self.display_map(cords)

    def reset(self):
        self.item_dict = {}
