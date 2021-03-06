"""Simplifies input with .lower()
and .strip()"""


# Function to check user input
def play_again():
    while True:
        replay = input("\nPress <enter> to play again, or <e> to exit"
                       "\n>>> ")

        # If user presses <enter>, program sends out a looping signal
        if replay == "":
            print("Playing again...")
            break
        # If user presses <e>, program ends
        elif replay.lower().strip() == "e":
            print("Exiting...")
            break
        # Else, question loops (I don't need to put an else statement in this case)


# Main
play_again()



