class Player:

    def __init__(self):
        self.cords = (0,0)

    @property
    def up(self):
        return self.cords[0], self.cords[1] - 1

    @property
    def right(self):
        return self.cords[0] + 1, self.cords[1]

    @property
    def down(self):
        return self.cords[0], self.cords[1] + 1

    @property
    def left(self):
        return self.cords[0] - 1, self.cords[1]

    def directions_dict(self):
        return {"UP": self.up, "RIGHT": self.right, "DOWN": self.down, "LEFT": self.left}
