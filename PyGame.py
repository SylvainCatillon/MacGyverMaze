import pygame as pg


class GameDisplay:
    """Use PyGame to display the MazeGyver game"""
    NB_FLOORS = (20, 13)  # Number of floors on the picture, as (number of columns, number of rows)

    def __init__(self, current_map):
        pg.init()
        self.current_map = current_map
        floors = pg.image.load("resources/floor-tiles-20x20.png")
        floor_width = floors.get_width() // self.NB_FLOORS[0]
        floor_height = floors.get_height() // self.NB_FLOORS[1]
        self.wall_image = pg.Surface((floor_width, floor_height))
        self.wall_image.blit(floors, (0, 0), (floor_width*14, floor_height*11, floor_width*15, floor_height*12))
        self.floor_image = pg.Surface((floor_width, floor_height))
        self.floor_image.blit(floors, (0, 0), (floor_width*8, floor_height*2, floor_width*9, floor_height*3))
        self.player_image = pg.Surface((floor_width, floor_height))
        self.screen = pg.display.set_mode((floor_width * current_map.width, floor_height * current_map.height))
        pg.display.set_caption("MazeGyver")
        self.rect_dict = {(x, y): pg.Rect(x*floor_width, y*floor_height, floor_width, floor_height)
                          for y in range(0, current_map.height) for x in range(0, current_map.width)}
        self.running = False

    def start(self):
        self.running = True
        self.create_map()
        self.start_player()
        pg.display.update()
        while self.running:
            for event in pg.event.get():
                available_directions = self.current_map.get_available_directions()
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    print("Keydown")
                    if event.key == pg.K_UP:
                        print("UP")
                        if "N" in available_directions:
                            self.move_player("N")
                    elif event.key == pg.K_RIGHT:
                        if "E" in available_directions:
                            self.move_player("E")
                    elif event.key == pg.K_DOWN:
                        if "S" in available_directions:
                            self.move_player("S")
                    elif event.key == pg.K_LEFT:
                        if "W" in available_directions:
                            self.move_player("W")
                    pg.display.update()

    def create_map(self):
        for cords, rect in self.rect_dict.items():
            if self.current_map.is_wall(cords):
                self.screen.blit(self.wall_image, rect)
            else:
                self.screen.blit(self.floor_image, rect)

    def start_player(self):
        load = pg.image.load("resources/MacGyver.png").convert_alpha()
        pg.transform.scale(load, (self.player_image.get_width(), self.player_image.get_height()), self.player_image)
        self.screen.blit(self.player_image, self.rect_dict[self.current_map.start])

    def move_player(self, direction):
        old_position = self.current_map.current_position
        self.current_map.set_current_position(direction)
        self.screen.blit(self.floor_image, self.rect_dict[old_position])
        self.screen.blit(self.player_image, self.rect_dict[self.current_map.current_position])











