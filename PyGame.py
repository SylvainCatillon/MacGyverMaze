import pygame as pg


class GameDisplay:

    def __init__(self, current_map):
        pg.init()
        self.current_map = current_map
        self.floors = pg.image.load("resources/floor-tiles-20x20.png")
        floor_size = self.floors.get_size()
        self.floor_width = floor_size[0] // 20
        self.floor_height = floor_size[1] // 13
        self.screen = pg.display.set_mode((self.floor_width * current_map.width, self.floor_height * current_map.height))
        pg.display.set_caption("MazeGyver")
        self.rect_list = [pg.Rect(i, y, self.floor_width, self.floor_height) for y in range(0, self.screen.get_size()[1], self.floor_height)
                          for i in range(0, self.screen.get_size()[0], self.floor_width)]
        for rect in self.rect_list:
            self.screen.blit(self.floors, rect, (0, 0, floor_size[0] / 20, floor_size[1] / 13))
        pg.display.update()
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    self.running = False




