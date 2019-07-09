import pygame as pg


class GameDisplay:
    """Use PyGame to display the MazeGyver game"""
    NB_FLOORS = (20, 13)  # Number of floors on the picture, as (number of columns, number of rows)

    def __init__(self, current_map):
        pg.init()
        self.current_map = current_map
        self.floors = pg.image.load("resources/floor-tiles-20x20.png")
        floor_size = self.floors.get_size()
        self.floor_width = floor_size[0] // self.NB_FLOORS[0]
        self.floor_height = floor_size[1] // self.NB_FLOORS[1]
        self.wall_image_cords = (self.floor_width*14, self.floor_height*11, self.floor_width*15, self.floor_height*12)  # Replace with variable
        self.floor_image_cords = (self.floor_width*8, self.floor_height*2, self.floor_width*9, self.floor_height*3)  # Replace with variable
        self.screen = pg.display.set_mode((self.floor_width * current_map.width, self.floor_height * current_map.height))
        pg.display.set_caption("MazeGyver")
        self.rect_dict = {(x, y): pg.Rect(x*self.floor_width, y*self.floor_height, self.floor_width, self.floor_height)
                          for y in range(0, current_map.height) for x in range(0, current_map.width)}
        self.running = False

    def start(self):
        self.running = True
        self.create_map()
        pg.display.update()
        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    self.running = False

    def create_map(self):
        for cords, rect in self.rect_dict.items():
            if self.current_map.is_wall(cords):
                print(cords)
                print(rect)
                self.screen.blit(self.floors, rect, self.wall_image_cords)
            else:
                self.screen.blit(self.floors, rect, self.floor_image_cords)





