import pygame as pg


class Input:
    """Class in charge of all the inputs of the game"""

    @property
    def game_input(self):
        """Input method to call when the game is running.
        Run until being able to return a correct input.
        Return "Q" for quit, or a direction ('UP', 'RIGHT', 'DOWN', 'LEFT')"""
        event = pg.event.wait()
        if event.type == pg.QUIT:
            return "Q"
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                return "Q"
            if event.key == pg.K_UP:
                return "UP"
            elif event.key == pg.K_RIGHT:
                return "RIGHT"
            elif event.key == pg.K_DOWN:
                return "DOWN"
            elif event.key == pg.K_LEFT:
                return "LEFT"
        return self.game_input

    @property
    def end_input(self):
        """Input method to call when the game is ending.
        Run until being able to return a correct input.
        Return True if the user wants to play again, False otherwise"""
        event = pg.event.wait()
        if event.type == pg.QUIT:
            return False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                return True
            if event.key == pg.K_ESCAPE:
                return False
        return self.end_input
