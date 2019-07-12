import pygame as pg


class GameDisplay:
    """Use PyGame to display the MazeGyver game"""
    NB_FLOORS = (20, 13)  # Number of floors on the picture, as (number of columns, number of rows)
    SQUARE_SIZE = (60, 60)  # Size of each square of the map, as (width, height)

    def __init__(self, game):
        pg.init()
        self.game = game
        self.screen = pg.Surface((1, 1))
        self.rect_dict = {}
        self.displayed_player_pos = (0, 0) # Changez nom
        self.image_dict = {}

    def load_items(self):
        for item in self.game.items_dict.values():
            file_name = "resources/{}.png".format(item.name)
            image = pg.image.load(file_name).convert_alpha()
            self.image_dict[item.symbol] = pg.transform.scale(image, self.SQUARE_SIZE)

    def init_display(self): # Repartir dans plusieurs fonctions. Une fonction par image, avec size en arg. Example load_items()
        floors = pg.image.load("resources/floor-tiles-20x20.png")
        floor_width = floors.get_width() // self.NB_FLOORS[0]
        floor_height = floors.get_height() // self.NB_FLOORS[1]
        self.screen = pg.display.set_mode((self.SQUARE_SIZE[0] * self.game.map.width, self.SQUARE_SIZE[1] * self.game.map.height))
        pg.display.set_caption("MazeGyver")
        wall_image = pg.Surface((floor_width, floor_height))
        wall_image.blit(floors, (0, 0), (floor_width * 14, floor_height * 11, floor_width * 15,
                                              floor_height * 12))  # Must be (floor_width*14, floor_height*11, floor_width, floor_height)
        self.image_dict[self.game.map.WALL] = pg.transform.scale(wall_image, self.SQUARE_SIZE)
        floor_image = pg.Surface((floor_width, floor_height))
        floor_image.blit(floors, (0, 0), (floor_width * 8, floor_height * 2, floor_width * 9,
                                               floor_height * 3))  # Must be (floor_width*8, floor_height*2, floor_width, floor_height))
        self.image_dict[self.game.map.FLOOR] = pg.transform.scale(floor_image, self.SQUARE_SIZE)
        player_image = pg.image.load("resources/MacGyver.png").convert_alpha()
        self.image_dict["player"] = pg.transform.scale(player_image, self.SQUARE_SIZE)
        keeper_image = pg.image.load("resources/Gardien.png").convert_alpha()
        self.image_dict["K"] = pg.transform.scale(keeper_image, self.SQUARE_SIZE)
        self.load_items()
        self.rect_dict = {(x, y): pg.Rect(x*self.SQUARE_SIZE[0], y*self.SQUARE_SIZE[1], self.SQUARE_SIZE[0], self.SQUARE_SIZE[1])
                          for y in range(0, self.game.map.height) for x in range(0, self.game.map.width)}

    def start(self):
        self.init_display()
        self.create_map()  #Afficher joueur dès création? ou par-dessus sol si tranparence
        self.start_player()
        pg.display.update()

    """def create_map(self):
        for cords, rect in self.rect_dict.items():
            if self.game.map.is_wall(cords):
                self.screen.blit(self.image_dict[self.game.map.WALL], rect)
            else:
                self.screen.blit(self.image_dict[self.game.map.FLOOR], rect)"""
    def create_map(self):
        for cords, rect in self.rect_dict.items():
            symbol = self.game.map.get_square(cords)
            if symbol == "S": # A changer. Start probablement inutile, changer dans map et display
                self.screen.blit(self.image_dict[self.game.map.FLOOR], rect)
            else:
                self.screen.blit(self.image_dict[symbol], rect)

    def start_player(self):
        self.screen.blit(self.image_dict["player"], self.rect_dict[self.game.map.start]) # change current_map.start par player.cords?
        self.displayed_player_pos = self.game.player.cords

    def move_player(self):
        old_rect = self.rect_dict[self.displayed_player_pos]
        new_rect = self.rect_dict[self.game.player.cords]
        self.screen.blit(self.image_dict[self.game.map.FLOOR], old_rect)
        self.screen.blit(self.image_dict["player"], new_rect)
        self.displayed_player_pos = self.game.player.cords
        pg.display.update([old_rect, new_rect])

    def item_collected(self, item_name):
        pass

    def end(self, victory):
        print(victory)

    def input(self):
        event = pg.event.wait()
        if event.type == pg.QUIT:
            return "Q"
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                return "UP"
            elif event.key == pg.K_RIGHT:
                return "RIGHT"
            elif event.key == pg.K_DOWN:
                return "DOWN"
            elif event.key == pg.K_LEFT:
                return "LEFT"
        return self.input()











