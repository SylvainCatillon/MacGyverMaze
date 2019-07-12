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

    def load_image(self, name):
        """Load an image from a png file in resources directory, scales it and put it in self.images_dict"""
        file_name = "resources/{}.png".format(name)
        image = pg.image.load(file_name).convert_alpha()
        self.image_dict[name[0].upper()] = pg.transform.scale(image, self.SQUARE_SIZE)

    def load_background(self, floor_index, wall_index):  # Use spritesheet?
        """Load the floor and wall images from a sprite sheet.
        Take for arguments floor_index and wall_index, the wall and floor location on the sprite sheet as
        a tuple (width pixel index, height pixel index)"""
        floors = pg.image.load("resources/floor-tiles-20x13.png")
        floor_width = floors.get_width() // self.NB_FLOORS[0]
        floor_height = floors.get_height() // self.NB_FLOORS[1]
        floor_image = pg.Surface((floor_width, floor_height))
        floor_image.blit(
            floors, (0, 0), (floor_width*floor_index[0], floor_height*floor_index[1], floor_width, floor_height))
        self.image_dict[self.game.map.FLOOR] = pg.transform.scale(floor_image, self.SQUARE_SIZE)
        wall_image = pg.Surface((floor_width, floor_height))
        wall_image.blit(
            floors, (0, 0), (floor_width*wall_index[0], floor_height*wall_index[1], floor_width, floor_height))
        self.image_dict[self.game.map.WALL] = pg.transform.scale(wall_image, self.SQUARE_SIZE)

    def init_display(self):
        """Initialize the screen and load the game images"""
        self.screen = pg.display.set_mode(
            (self.SQUARE_SIZE[0]*self.game.map.width, self.SQUARE_SIZE[1]*self.game.map.height))
        pg.display.set_caption("MazeGyver")
        self.load_background((8, 2), (14, 11))
        self.load_image("Player")
        self.load_image("Keeper")
        for item in self.game.items_dict.values():
            self.load_image(item.name)
        pg.display.set_icon(self.image_dict["P"]) # Remplacer par tile Crusader?
        self.rect_dict = {
            (x, y): pg.Rect(x*self.SQUARE_SIZE[0], y*self.SQUARE_SIZE[1], self.SQUARE_SIZE[0], self.SQUARE_SIZE[1])
            for y in range(0, self.game.map.height) for x in range(0, self.game.map.width)}

    def start(self):
        self.init_display()
        self.create_map()
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
            if symbol == "K":  # To display floor below the keeper and allow transparency
                self.screen.blit(self.image_dict[self.game.map.FLOOR], rect)
            self.screen.blit(self.image_dict[symbol], rect)

    def start_player(self):
        self.screen.blit(self.image_dict["P"], self.rect_dict[self.game.player.cords]) # change player.cords par current_map.start?
        self.displayed_player_pos = self.game.player.cords

    def move_player(self):
        old_rect = self.rect_dict[self.displayed_player_pos]
        new_rect = self.rect_dict[self.game.player.cords]
        self.screen.blit(self.image_dict[self.game.map.FLOOR], old_rect)
        self.screen.blit(self.image_dict["P"], new_rect)
        self.displayed_player_pos = self.game.player.cords
        pg.display.update([old_rect, new_rect])

    def item_collected(self, item_name):
        # pg.time.display(1000)
        # Text item_collected
        rect = self.rect_dict[self.game.player.cords]
        self.screen.blit(self.image_dict[self.game.map.FLOOR], rect)
        self.screen.blit(self.image_dict["P"], rect)
        pg.display.update(rect)

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











