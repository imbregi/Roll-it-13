import random


# generates random number (1-6)
def roll_die():
    result = random.randint(1, 6)
    return result


# Main Routine
die_roll = roll_die()
print(die_roll)
