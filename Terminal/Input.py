class Input:

    @staticmethod
    def pave_num(inp):
        """Method to convert input into direction"""
        return inp.replace("4", "LEFT").replace("8", "UP").\
            replace("2", "DOWN").replace("6", "RIGHT")

    @property
    def game_input(self):
        """Method to get input during the game"""
        inp = ""
        while inp not in ["DOWN", "RIGHT", "UP", "LEFT"]:
            inp = input("Choose a direction").upper()
            if inp == "Q":
                break
            inp = self.pave_num(inp)
        return inp

    @property
    def end_input(self):
        """Method to get input at the end of the game"""
        inp = input()
        if inp.upper() == "Q":
            return False
        if inp == "" \
                  "":
            return True
        return self.end_input
