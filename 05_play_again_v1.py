"""Yes/no checker to check whether
 the user wants to play again"""


# Function to check user input
def play_again():
    while True:
        replay = input("\nPress <enter> to play again, or <e> to exit"
                       "\n>>> ")

        # If user presses <enter>, program sends out a looping signal
        if replay == "":
            repeat = True
            print("Playing again...")
            break
        # If user presses <e>, program ends
        elif replay == "e":
            repeat = False
            print("Exiting...")
            break
        # Else, question loops (I don't need to put an else statement in this case)


play_again()



