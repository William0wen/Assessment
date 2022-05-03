"""Puts 01_ask_question_v1 into a loop with a test output
Also tidies up the code by adding \n for a new line"""

score = 0

while True:
    # Ask question
    question = input("\nWhat is the Maori word for Tuesday? ").lower().strip()

    # If answer is correct, continue
    if question == "ratu":
        print("Program continues, 1 point added")
        score += 1
        print(f"score: {score}")
        print(question)

    # Else, score stays the same, continue
    else:
        print("Wrong answer!")
        print(f"score: {score}")
        print(question)

