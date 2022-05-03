"""Puts 02_yes_no_v2 into a re-usable function"""


def ask(question_text, answer):
    while True:
        # Ask if played before
        question = input(question_text).lower().strip()

        # If y, continue
        if question == "yes" or question == "y":
            print("Program continues\n")
            return question

        # If n, display instructions
        elif question == "no" or question == "n":
            print("display instructions\n")
            return question

        # Else, ask again
        else:
            print("Please type [yes] or [no]\n")


ask("Have you played this game before? ", "")


