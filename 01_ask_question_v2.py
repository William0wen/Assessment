"""Puts 02_yes_no_v1 into a loop with a test output"""

while True:
    # Ask if played before
    show_instructions = input("Have you played this game before? ").lower().strip()

    # If y, continue
    if show_instructions == "y" or show_instructions == "yes":
        print("Program continues\n")

    # If n, display instructions
    elif show_instructions == "n" or show_instructions == "no":
        print("display instructions\n")

    # Else, ask again
    else:
        print("Please type [yes] or [no]\n")

