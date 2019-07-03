
class Display:
    """The class in charge of the display"""

    LANGUAGE_DICT = {
        "english": {
            "welcome": "Welcome in the MazeGyver Game! Will you be able to get out of here?",
            "congrats": "Congratulations, you reached the exit!!!",
            "game_over": "How unfortunate, you're dead!",
            "end": "Thank you for playing"
        }
    }

    def __init__(self, language, current_map):
        self.language_dict = self.LANGUAGE_DICT[language]
        self.current_map = current_map

    @property
    def welcome(self):
        return self.language_dict["welcome"]

    @property
    def congrats(self):
        return self.language_dict["congrats"]

    @property
    def game_over(self):
        return self.language_dict["game_over"]

    @property
    def end(self):
        return self.language_dict["end"]

    def display_map(self):
        display_string = ""
        for y in range(self.current_map.height):
            for x in range(self.current_map.width):
                display_string += self.current_map.get_square((x, y))
            display_string += "\n"
        print(display_string)




