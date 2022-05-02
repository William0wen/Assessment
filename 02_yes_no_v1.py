"""Asks for users input, if n, do instructions,
if y, skip instructions.
Uses .lower() and .strip() to simplify input"""

# Ask if played before
show_instructions = input("Have you played this game before? ").lower().strip()

if show_instructions == "y" or show_instructions == "yes":
    print("Program continues")

elif show_

