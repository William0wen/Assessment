"""Asks for users input, if n, do instructions,
if y, skip instructions.
Uses .lower() and .strip() to simplify input"""

# Ask if played before
show_instructions = input("Have you played this game before? ").lower().strip()

# If y, continue
if show_instructions == "y" or show_instructions == "yes":
    print("Program continues")

# If n, display instructions
elif show_instructions == "n" or "no":
    print("display instructions")

# Else, ask again
else:
    print("Please type [yes] or [no]")

