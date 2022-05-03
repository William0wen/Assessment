"""Asks for users input, if the answer
is right, 1 point is added.
Else, print "Wrong Answer!"
Uses .lower() and .strip() to simplify input"""

score = 0

# Ask question
question = input("What is the Maori word for Tuesday? ").lower().strip()

# If answer is correct, continue
if question == "ratu":
    print("Program continues, 1 point added")
    score += 1

# Else, score stays the same, continue
else:
    print("Wrong answer!")

