# create a dictionary which will count the items held by each triad of elves

inventory = {}
sack_queue = []
priority_sum = 0

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


def group_checker(sacks):
	"""
	Checks for a common item amongst all sacks passed
	"""

	for item in sacks[0]:
		if item in sacks[1]:
			if item in sacks[2]:
				return prioritize(item)



with open("input.txt", "r") as f:
	try:
		all_sacks = [line for line in f]
		counter = 0

	finally:
		f.close()
		
for sack in all_sacks:
	sack_queue.append(sack)
	
	if counter % 3 == 2:
		item_priority = group_checker(sack_queue)
		priority_sum += item_priority
		sack_queue = []

	counter += 1

print(f"final: {priority_sum}")