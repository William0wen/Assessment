"""Generates a random question out of
a list of questions and answers, using 01_ask_question_v3"""

# List of questions and answers, stored in a dictionary
questions = ["What is the Maori word for Monday? ",
             "What is the Maori word for Tuesday? ",
             "What is the Maori word for Wednesday? ",
             "What is the Maori word for Thursday? ",
             "What is the Maori word for Friday? ",
             "What is the Maori word for Saturday? ",
             "What is the Maori word for Sunday? "]

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


