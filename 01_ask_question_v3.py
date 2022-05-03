"""Puts 01_ask_question_v2 into a re-usable function"""

score = 0


def ask(question_text, answer):
    global score
    while True:
        # Ask question
        question = input("\nWhat is the Maori word for Tuesday? ").lower().strip()

        # If answer is correct, continue
        if question == answer:
            print("Program continues, 1 point added")
            score += 1
            print(f"score: {score}")
            print(question)

        # Else, score stays the same, continue
        else:
            print("Wrong answer!")
            print(f"score: {score}")
            print(question)


ask("What is the Maori word for Tuesday? ", "ratu")


