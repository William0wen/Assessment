"""Loops 02_gen_rand_number 7 times, so that
every question has a chance of appearing"""

import random

# List of questions and answers, stored in dictionaries
questions = [{"day": "Monday", "answer": "rahina"},
             {"day": "Tuesday", "answer": "ratu"},
             {"day": "Wednesday", "answer": "raapa"},
             {"day": "Thursday", "answer": "rapare"},
             {"day": "Friday", "answer": "ramere"},
             {"day": "Saturday", "answer": "rahoroi"},
             {"day": "Sunday", "answer": "ratapu"}]

# Generating random question out of the list of questions

score = 0


# Ask question function
def ask(question_text, answer):
    global score
    # Ask question
    question = input(f"What is the Maori word for {question_text}? ").lower().strip()

    # If answer is correct, continue
    if question == answer:
        print("\nCorrect!")
        score += 1
        print(f"score: {score}\n")

    # Else, score stays the same, continue
    else:
        print("\nWrong answer!")
        print(f"score: {score}\n")


# Main

# Repeating the round 7 times
for number in range(1, 8):
    # Generating random question out of the list of questions
    random_question = random.choice(questions)
    rand_day = random_question["day"]
    rand_answer = random_question["answer"]

    ask(rand_day, rand_answer)




