"""Generates a random question out of
a list of questions and answers, using 01_ask_question_v3"""

import random

# List of questions and answers, stored in dictionaries
questions = [{"day": "Monday", "answer": "Rahina"},
             {"day": "Tuesday", "answer": "Ratu"},
             {"day": "Wednesday", "answer": "Raapa"}]

score = 0

random_question = random.choice(questions)
print(random_question)


def ask(question_text, answer):
    global score
    while True:
        # Ask question
        question = input(f"What is the Maori word for {question_text}? ").lower().strip()

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





