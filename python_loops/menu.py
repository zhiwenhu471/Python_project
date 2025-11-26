def display_menu(options):
    print("Main Menu:")
    for pos, option in enumerate(options, start=1):  # the number starts from 0
        print(f"{pos}. {option}")


display_menu(["Open", "Save", "Settings", "Quit"])
