import pygame as pg


class Display:
    """Use PyGame to display the MazeGyver game"""
    NB_FLOORS = (20, 13)  # Number of floors on the floors file, as (number of columns, number of rows)
    FLOOR_INDEX = (14, 6)  # Index of the chosen floor image on the floors file
    WALL_INDEX = (14, 11)  # Index of the chosen wall image on the floors file
    SCREEN_SIZE = (int(900), int(900))  # Size of the screen, as (width, height)
    INVENTORY = True  # Set it to True for having an inventory
    TEXT_COLOR = (255, 255, 255)  # Color of the text, as (red index, green index, blue index)
    WELCOME_TEXT = "Welcome!!! You have to found {} items"
    VICTORY_TEXT = "Congratulations!\nYou sent the keeper to sleep\nand reached the exit!!!"
    DEFEAT_TEXT = "You tried to run trough\nthe keeper without the items,\nso he crushed your head! Sorry!"
    END_TEXT = "Press enter to play again, escape to quit"

    def __init__(self, game):
        """Constructor of Display. Take the current game for argument"""
        pg.init()
        self.square_size = (1, 1)
        self.game = game
        self.font = pg.font.Font(None, self.square_size[1])
        self.screen = pg.Surface((1, 1))
        self.floor_rect_dict = {}
        self.wall_rect_dict = {}
        if self.INVENTORY:
            self.items_found = 0
            self.inventory_rect_list = []
        self.displayed_player_pos = (0, 0)
        self.image_dict = {}
        pg.key.set_repeat(350, 60)

    @property
    def square_width(self):
        return self.square_size[0]

    @property
    def square_height(self):
        return self.square_size[1]

    def init_screen(self):
        """Initialize the screen"""
        #  adapted_screen_size use modulo to assure that the screen_size is a multiple of map.width and map.height
        adapted_screen_size = (self.SCREEN_SIZE[0]-(self.SCREEN_SIZE[0] % self.game.map.width),
                               self.SCREEN_SIZE[1]-(self.SCREEN_SIZE[1] % self.game.map.height))
        self.screen = pg.display.set_mode(adapted_screen_size)
        pg.display.set_caption("MazeGyver")
        self.square_size = (adapted_screen_size[0]//self.game.map.width, adapted_screen_size[1]//self.game.map.height)
        self.font = pg.font.Font(None, self.square_height)
        pg.display.set_icon(pg.image.load("resources/tile-crusader-logo.png"))
        self.floor_rect_dict = {
            (x, y): pg.Rect(x*self.square_width, y*self. square_height, self.square_width, self. square_height)
            for (x, y) in self.game.map.floor_list}
        self.wall_rect_dict = {
            (x, y): pg.Rect(x * self.square_width, y * self. square_height, self.square_width, self. square_height)
            for (x, y) in self.game.map.wall_list}

    def load_image(self, name):
        """Load an image from a png file in resources directory, scales it and put it in self.images_dict"""
        file_name = "resources/{}.png".format(name)
        image = pg.image.load(file_name).convert_alpha()
        self.image_dict[name.lower()] = pg.transform.scale(image, self.square_size)

    def load_background(self):  # Use spritesheet?
        """Load the floor and wall images from a sprite sheet.
        Take for arguments floor_index and wall_index, the wall and floor location on the sprite sheet as
        a tuple (width pixel index, height pixel index)"""
        floors = pg.image.load("resources/floor-tiles-20x13.png")
        floor_width = floors.get_width() // self.NB_FLOORS[0]
        floor_height = floors.get_height() // self.NB_FLOORS[1]
        floor_image = pg.Surface((floor_width, floor_height))
        floor_image.blit(floors, (0, 0),
                         (floor_width*self.FLOOR_INDEX[0], floor_height*self.FLOOR_INDEX[1], floor_width, floor_height))
        self.image_dict["floor"] = pg.transform.scale(floor_image, self.square_size)
        wall_image = pg.Surface((floor_width, floor_height))
        wall_image.blit(floors, (0, 0),
                        (floor_width*self.WALL_INDEX[0], floor_height*self.WALL_INDEX[1], floor_width, floor_height))
        self.image_dict["wall"] = pg.transform.scale(wall_image, self.square_size)

    def prepare_inventory(self):
        """Prepare an inventory to be displayed.
        Inventory is a line at the bottom of the screen which display a welcome message at the start.
        Every time an item is found, a message and the image of the item can be displayed in the inventory"""
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        text_width = screen_width-self.square_width*len(self.game.items_list)
        self.inventory_rect_list.append(pg.Rect(0, screen_height, text_width, self.square_height))
        for i in range(len(self.game.items_list)):
            self.inventory_rect_list.append(
                pg.Rect(text_width + self.square_width*i, screen_height, self.square_width, self. square_height))
        self.screen = pg.display.set_mode((screen_width, screen_height+self. square_height))
        text_surf = self.font.render(self.WELCOME_TEXT.format(len(self.game.items_list)), True, self.TEXT_COLOR)
        text_rect = self.inventory_rect_list[0]
        if text_surf.get_width() > text_rect.width:
            text_surf = pg.transform.scale(text_surf, (text_rect.width, text_surf.get_height()))
        self.screen.blit(text_surf, text_rect)

    def prepare_map(self):
        """Prepare the map to be displayed on the screen"""
        for floor_rect in self.floor_rect_dict.values():
            self.screen.blit(self.image_dict["floor"], floor_rect)
        for wall_rect in self.wall_rect_dict.values():
            self.screen.blit(self.image_dict["wall"], wall_rect)
        self.screen.blit(self.image_dict["keeper"], self.floor_rect_dict[self.game.map.keeper])
        self.screen.blit(self.image_dict["player"],
                         self.floor_rect_dict[self.game.player.cords])  # change player.cords par current_map.start?
        self.displayed_player_pos = self.game.player.cords

    def prepare_item(self, item):
        """Load the image of an item, and prepare it to be displayed on screen.
        Take an Object Item as argument"""
        self.load_image(item.name)
        self.screen.blit(self.image_dict[item.name.lower()], self.floor_rect_dict[item.cords])

    def start(self):
        """Call the methods to:
        -Initialize the screen
        -Load the images
        -Prepare the Display of the Map
        -Update the screen"""
        self.init_screen()
        self.load_background()
        self.load_image("Player")
        self.load_image("Keeper")
        if self.INVENTORY:
            self.prepare_inventory()
        self.prepare_map()
        for item in self.game.items_list:
            self.prepare_item(item)
        pg.display.update()

    def move_player(self):
        """Update the screen to follow player movement"""
        old_rect = self.floor_rect_dict[self.displayed_player_pos]
        new_rect = self.floor_rect_dict[self.game.player.cords]
        self.screen.blit(self.image_dict["floor"], old_rect)
        self.screen.blit(self.image_dict["player"], new_rect)
        self.displayed_player_pos = self.game.player.cords
        pg.display.update([old_rect, new_rect])

    def item_collected(self, item_name):
        """Update the screen to delete collected item.
        If Inventory is on, display a message and add the item in the inventory"""
        if self.INVENTORY:
            self.items_found += 1
            text_rect = self.inventory_rect_list[0]
            item_rect = self.inventory_rect_list[self.items_found]
            text_surf = pg.Surface(text_rect.size)
            text_surf.blit(self.font.render("Item collected: " + item_name, True, self.TEXT_COLOR), (0, 0))
            self.screen.blit(text_surf, text_rect)
            self.screen.blit(self.image_dict[item_name.lower()], item_rect)
            pg.display.update([text_rect, item_rect])
        rect = self.floor_rect_dict[self.game.player.cords]
        self.screen.blit(self.image_dict["floor"], rect)
        self.screen.blit(self.image_dict["player"], rect)
        pg.display.update(rect)

    def prepare_end_screen(self, text):
        """Prepare the end screen. Take the text to be displayed for argument"""
        end_screen = pg.Surface(self.screen.get_size())
        lines_list = text.split("\n")
        for i, line in enumerate(lines_list):
            text_surf = self.font.render(line, True, self.TEXT_COLOR)
            text_height = text_surf.get_height()
            if text_surf.get_width() > end_screen.get_width():
                text_surf = pg.transform.scale(text_surf, (end_screen.get_width(), text_height))
            text_width = text_surf.get_width()
            x_cord = end_screen.get_width()/2 - text_width/2
            y_cord = end_screen.get_height()/2 - ((len(lines_list)*text_height)/2 - i*text_height)
            end_screen.blit(text_surf, (x_cord, y_cord))
        self.screen.blit(end_screen, (0, 0))

    def end(self, victory):
        """Call end_screen() with the right text to prepare end_screen, and display it"""
        if victory:
            self.prepare_end_screen(self.VICTORY_TEXT + "\n\n" + self.END_TEXT)
        else:
            self.prepare_end_screen(self.DEFEAT_TEXT + "\n\n" + self.END_TEXT)
        pg.display.update()
