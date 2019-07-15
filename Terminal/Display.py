class Display:
    """The class in charge of the display"""

    LANGUAGE_DICT = {
        "english": {
            "welcome": "Welcome in the MazeGyver Game! Will you be able to get out of here?",
            "congrats": "Congratulations, you sent the keeper to sleep and reached the exit!!!",
            "death": "You tried to run trough the keeper without the items, so he crushed your head! Sorry!",
            "end": "Thank you for playing",
            "collected": "Well played, you collected: "
        },
        "francais": {
            "welcome": "Bienvenue dans le jeu MazeGyver! Trouverez-vous la sortie?",
            "congrats": "Bravo, vous avez endormi le gardien et êtes sorti vivant du labyrinthe!!!",
            "death": "Vous avez essayé de passer le gardien sans les bons objets, il vous a applati la tête! dommage!",
            "end": "Merci d'avoir joué.",
            "collected": "Bien joué, vous avez rammassé: "
        }
    }

    def __init__(self, game):
        self.language_dict = self.LANGUAGE_DICT["english"]
        self.game = game

    @property
    def available_languages(self):
        return self.LANGUAGE_DICT.keys()

    def welcome(self):
        print(self.language_dict["welcome"])

    def congrats(self):
        print(self.language_dict["congrats"])

    def death(self):
        print(self.language_dict["death"])

    def end(self, victory):
        if victory:
            print(self.language_dict["congrats"])
        else:
            print(self.language_dict["death"])
        print(self.language_dict["end"])

    def choose_language(self, language):
        self.language_dict = self.LANGUAGE_DICT[language]

    def item_collected(self, item_name):
        print(self.language_dict["collected"] + item_name)

    def display_map(self):
        display_string = ""
        for y in range(self.game.map.height):
            for x in range(self.game.map.width):
                if (x, y) == self.game.player.cords:
                    display_string += "P"
                else:
                    display_string += self.game.map.get_square((x, y)).replace("F", " ").replace("W", "|")
            display_string += "\n"
        print(display_string)

    def start(self):
        self.choose_language("english")  # add input
        self.welcome()
        self.display_map()

    def move_player(self):
        self.display_map()