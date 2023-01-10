"""Solutions for Day 9 of the Advent of Code 2022"""

current_head = (0,0)
current_tail = (0,0)
tail_history = [(0,0)]

# For importing and cleaning the puzzle input
def read_puzzle_input(file_name):
	cleaned_input = []

	with open(file_name, "r") as f:
		try:
			cleaned_input = [
				tuple(
					int(c) if c.isdigit() else c for c in line.strip("\n").split()
				) for line in f
			]

		finally:
			f.close()

	return cleaned_input


# For moving the head based on movements given
def move_head(current_head, direction):
	"""
	Moves the current head incrementally either left, right, up, or down by
	incrementing the X or Y in coordinates as (X,Y)
	"""

	if direction == "U":
		return tuple([current_head[0], current_head[1] + 1])
	elif direction == "D":
		return tuple([current_head[0], current_head[1] - 1])
	elif direction == "L":
		return tuple([current_head[0] - 1, current_head[1]])
	elif direction == "R":
		return tuple([current_head[0] + 1, current_head[1]])
	else:
		return "Error: inappropriate direction given"

# To track the tail (determined by distance and directon to head)
def tail_check(head, tail):
	"""
	Returns the current tail position again if it is within one space of the
	head otherwise returns a new tail position (closer to the head) based on
	the rules given in the puzzle.
	"""

	lateral_movement = head[0] - tail[0]
	lateral_close = abs(lateral_movement) <= 1
	vertical_movement = head[1] - tail[1]
	vertical_close = abs(vertical_movement) <= 1


	if lateral_close and vertical_close:
		return current_tail
	elif lateral_close:
		if lateral_movement == 0:
			return tuple([tail[0], sum([tail[1], vertical_movement/2])])
		else:
			return tuple(
					[
						sum([tail[0], lateral_movement]),
						sum([tail[1], vertical_movement/2])
					]
				)
	elif vertical_close:
		if vertical_movement == 0:
			return tuple([sum([tail[0], lateral_movement/2]), tail[1]])
		else:
			return tuple(
					[
						sum([tail[0], lateral_movement/2]),
						sum([tail[1], vertical_movement])
					]
				)
	else:
		return("Error: head has moveed too far without tail moving.")

# To move the rope based on head movemments given in the input
def read_movement(movement):
	global current_head
	global current_tail
	direction = movement[0]
	distance = movement[1]

	for n in range(distance):
		current_head = move_head(current_head, direction)
		current_tail = tail_check(current_head, current_tail)
		tail_history.append(current_tail)


# Call the functions when the file is run from the command line
if __name__ == "__main__":
	# Read the file and prep for processing
	head_movements = read_puzzle_input("input.txt")

	# Call the function(s) to move the rope
	for movement in head_movements:
		read_movement(movement)

	# Calculate the nuber of positions the tail has visited and print
	print(f"Tail of the rope has been to {len(set(tail_history))} positions")
