"""Day three, first puzzle."""

def prioritize(char):
    """
    Takes in a character and return the "priority" as defined by the puzzle:
        -Lowercase item types a through z have priorities 1 through 26.
        -Uppercase item types A through Z have priorities 27 through 52.

    Inputs:
        char - a single character as a string

    Returns:
        priority - an integer representing the "priority" of the character
    """

    if char.islower():
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38

    return priority

with open("input.txt", "r") as f:
    try:
        doubles = 0
        sacks = []

        for sack in f:
            sack_cap = len(sack)
            compartment_cap = sack_cap // 2
            compartment_1 = sack[:compartment_cap]
            compartment_2 = sack[compartment_cap:]
            sacks.append([compartment_1, compartment_2])

            for item in compartment_1:
                if item in compartment_2:
                    doubles += prioritize(item)
                    break

        print(doubles)

    finally:
        f.close()