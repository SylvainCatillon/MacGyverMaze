display_config = dict(
    nb_floors=(20, 13),  # Number of sprites on the sheet: (columns, rows)
    floor_index=(14, 6),  # Index of the floor image on the floors file
    wall_index=(14, 11),  # Index of the wall image on the floors file
    screen_size=(int(800), int(800)),  # Size of the screen: (width, height)
    inventory=True,  # Set it to True for having an inventory
    text_color=(255, 255, 255),  # (red index, green index, blue index)
    welcome_text="Welcome! You have to find {} items",
    item_collected="Item collected: ",
    victory_text="Congratulations!\nYou sent the keeper to sleep\n"
                 "and reached the exit!!!",
    defeat_text="You tried to run trough\nthe keeper without the items,"
                "\nso he crushed your head! Sorry!",
    end_text="Press enter to play again, escape to quit"
)

map_config = dict(
    symbol_dict={
        "floor": "F",
        "wall": "W",
        "start": "S",
        "keeper": "K"}
)

game_config = dict(
    item_names_list=["Needle", "Tube", "Ether"],
    use_pygame=True
)
