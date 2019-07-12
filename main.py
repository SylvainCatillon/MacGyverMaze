from Game import *

if __name__ == "__main__":
    while Game.CONTINUE:
        newGame = Game()
        newGame.play()
        del newGame #  Judicieux?
