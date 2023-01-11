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
def read_movement(movement, part_2=False):
	direction = movement[0]
	distance = movement[1]

	if part_2:
		global head

		for n in range(distance):
			head.move_knot(direction, head=True)

	else:
		global current_head
		global current_tail

		for n in range(distance):
			current_head = move_head(current_head, direction)
			current_tail = tail_check(current_head, current_tail)
			tail_history.append(current_tail)

# Create a knot class for all knots which will keep track of their own position
# "Head" type will function differently

class Knot:
	def __init__(self):
		self.position = (0,0)
		self.position_history = [(0,0)]
		self.previous = None
		self.next = None

	def move_knot(self, direction, head=False):
		if direction == "U":
			self.position = tuple([self.position[0], self.position[1] + 1])
		elif direction == "D":
			self.position = tuple([self.position[0], self.position[1] - 1])
		elif direction == "L":
			self.position = tuple([self.position[0] - 1, self.position[1]])
		elif direction == "R":
			self.position = tuple([self.position[0] + 1, self.position[1]])
		else:
			print("Error: inappropriate direction given")

		if head:
			self.position_history.append(self.position)
			self.next.check_follow(self.position)

	def check_follow(self, previous):
		lateral_movement = previous[0] - self.position[0]
		lateral_close = abs(lateral_movement) <= 1
		vertical_movement = previous[1] - self.position[1]
		vertical_close = abs(vertical_movement) <= 1


		if lateral_close and vertical_close:
			pass
		elif lateral_close:
			if lateral_movement == 0:
				if vertical_movement < 0:
					self.move_knot("D")
				else:
					self.move_knot("U")
			else:
				self.position = tuple(
						[
							int(sum([self.position[0], lateral_movement])),
							int(sum([self.position[1], vertical_movement/2]))
						]
					)
		elif vertical_close:
			if vertical_movement == 0:
				if lateral_movement < 0:
					self.move_knot("L")
				else:
					self.move_knot("R")
			else:
				self.position = tuple(
						[
							int(sum([self.position[0], lateral_movement/2])),
							int(sum([self.position[1], vertical_movement]))
						]
					)
		else:
			self.position = tuple(
					[
						int(sum([self.position[0], lateral_movement/2])),
						int(sum([self.position[1], vertical_movement/2]))
					]
				)

		self.position_history.append(self.position)

		if self.next:
			self.next.check_follow(self.position)


# Call the functions when the file is run from the command line
if __name__ == "__main__":
	# Read the file and prep for processing
	head_movements = read_puzzle_input("input.txt")

	# #Part 1
	# # Call the function(s) to move the rope
	# for movement in head_movements:
	# 	read_movement(movement)

	# # Calculate the nuber of positions the tail has visited and print
	# print(f"Tail of the rope has been to {len(set(tail_history))} positions")


	# Part 2
	head = Knot()
	previous = None
	current = head
	last = None

	for n in range(9):
		current.previous = previous
		current.next = Knot()
		previous = current
		current = current.next

	for movement in head_movements:
		read_movement(movement, part_2=True)

	print(f"Tail of the rope has been to {len(set(current.position_history))} positions")

