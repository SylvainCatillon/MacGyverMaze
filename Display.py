
class Display:
    """The class in charge of the display"""

    LANGUAGE_DICT = {
        "english": {
            "welcome": "Welcome in the MazeGyver Game! Will you be able to get out of here?",
            "congrats": "Congratulations, you reached the exit!!!",
            "game_over": "How unfortunate, you're dead!",
            "end": "Thank you for playing"
        },
        "francais": {
            "welcome": "Bienvenue dans le jeu MazeGyver! Trouverez-vous la sortie?",
            "congrats": "Bravo, vous êtes sorti vivant du labyrinthe!!!",
            "game_over": "Dommage, vous êtes mort!",
            "end": "Merci d'avoir joué."
        }
    }

    def __init__(self, current_map):
        self.language_dict = self.LANGUAGE_DICT["english"]
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

    @property
    def available_languages(self):
        return self.LANGUAGE_DICT.keys()

    def choose_language(self, language):
        self.language_dict = self.LANGUAGE_DICT[language]

    def say_welcome(self):
        print(self.welcome)

    def display_map(self):
        display_string = ""
        for y in range(self.current_map.height):
            for x in range(self.current_map.width):
                display_string += self.current_map.get_square((x, y))
            display_string += "\n"
        print(display_string)




