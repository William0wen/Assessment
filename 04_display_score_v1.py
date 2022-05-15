"""Draws the user's attention to the final score."""

import random

# List of questions and answers, stored in dictionaries
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


# Ask question function
def ask(question_text, answer_):
    global score
    # Ask question
    question = input(f"What is the Maori word for {question_text}? ").lower().strip()

    # If answer is correct, continue
    if question == answer_:
        print("\nCorrect!")
        score += 1
        print(f"score: {score}\n")

    # Else, score stays the same, continue
    else:
        print("\nWrong answer!\n")


# Main

# Repeating the round 7 times
for number in range(0, 7):
    # Generating random question out of the list of questions
    random_question = random.choice(questions)
    rand_day = random_question["day"]
    rand_answer = random_question["answer"]

    # Assigning the beforehand score to a variable
    before_score = score

    # question loop
    ask(rand_day, rand_answer)

    # If the score hasn't changed, the question answer is added to a wrong_answers list
    if score == before_score:
        wrong_answers.append(random_question.pop("answer"))

    # removing the question that has already been asked.
    questions.remove(random_question)

print(f"\nYour final score is:\n\t*** {score}/7! ***")

if len(wrong_answers) == 0:
    print("\nCongratulations, you got every question correct!")
else:
    print(f"\nWrong answers:")
    for answer in wrong_answers:
        print(wrong_answers, end=" ")
