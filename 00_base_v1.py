"""Maori Quiz base program by William Owen
Meets PEP8 requirements"""

import random

replay_ = True


# Ask question function
def ask(question_text, answer_):
    global score
    # Ask question
    question = input(f"What is the Maori word for "
                     f"{question_text}? ").lower().strip()

    # If answer is correct, continue
    if question == answer_:
        print("\nCorrect!")
        score += 1
        print(f"score: {score}\n")

    # Else, score stays the same, continue
    else:
        print("\nWrong answer!\n")


# Function to check user input (for y/n)
def play_again():
    global replay_
    while True:
        replay = input("\n\nPress <enter> to play again, or <e> to exit."
                       "\n>>> ")

        # If user presses <enter>, program sets looping to true
        if replay == "":
            break
        # If user presses <e>, looping is false and program ends
        elif replay.lower().strip() == "e":
            replay_ = False
            break
        # Else, question loops
        # (I don't need to put an else statement in this case)


# Main

print("*** Welcome to the Maori Days of the Week Quiz! ***"
      "\n\nType in the correct answer to each of the 7 questions!"
      "\nWhen you type your answer, don't use any diacritics! "
      "(Marks above the letters)"
      "\nHopefully you will learn something new!\n")

while replay_:

    # List of questions and answers, stored in a list
    questions = [{"day": "Monday", "answer": "rahina"},
                 {"day": "Tuesday", "answer": "ratu"},
                 {"day": "Wednesday", "answer": "raapa"},
                 {"day": "Thursday", "answer": "rapare"},
                 {"day": "Friday", "answer": "ramere"},
                 {"day": "Saturday", "answer": "rahoroi"},
                 {"day": "Sunday", "answer": "ratapu"}]

    # List that contains the answers the user gets wrong
    wrong_answers = []

    score = 0

    # Loop for repeating the round 7 times
    for number in range(1, 8):
        print(f"\nQuestion {number}:")
        # Generating random question out of the list of questions
        random_question = random.choice(questions)
        rand_day = random_question["day"]
        rand_answer = random_question["answer"]

        # Assigning the beforehand score to a variable
        before_score = score

        # question loop
        ask(rand_day, rand_answer)

        # If the score hasn't changed, the question answer is
        # added to a wrong_answers list
        if score == before_score:
            wrong_answers.append(random_question.pop("answer"))

        # removing the question that has already been asked.
        questions.remove(random_question)

    print(f"\nYour final score is:\n\t*** {score}/7! ***")

    if len(wrong_answers) == 0:
        print("\nCongratulations, you got every question correct!")
    else:
        print(f"\nThe correct answers were:")
        for wrong_answer in wrong_answers:
            print(wrong_answer.title(), end="   ")

    play_again()

print("\n\n*** Thank you for playing the Maori Quiz! ***")
