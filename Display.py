
class Display:
    """The class in charge of the display"""

    english = {
        "welcome": "Welcome in the MazeGyver Game! Will you be able to get out of here?",
        "congrats": "Congratulations, you reached the exit!!!" ,
        "game_over": "How unfortunate, you're dead!",
        "end": "Thank you for playing"
    }

def display_map(current_map):
    display_string = ""
    for y in range(current_map.height):
        for x in range(current_map.width):
            display_string += current_map.get_square((x, y))
        display_string += "\n"
    print(display_string)


