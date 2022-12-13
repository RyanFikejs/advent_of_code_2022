"""Day 5 puzzles for Advent of Code 2022"""

# Suspect I can setup stacks (data structure) for this one

drawing = []
instructions = []
stacks = []
crane_type = 9001

# Open and separate the drawing from moving instructions
with open("input.txt", "r") as f:
	try:
		for line in f:
			line = line.strip("\n")

			if line[:4] == "move":
				instructions.append(line)
			else:
				drawing.append(line)

		drawing = drawing[:-1]

	finally:
		f.close()


# Build function to setup stacks from the drawing input
def build_stacks(drawing_input):
	for line in drawing_input[::-1]:
		for ind, char in enumerate(line):
			if ind % 4 == 1: 
				if char != " ":
					ref = ind // 4
					if char.isdigit():
						stacks.append([])
					else:
						stacks[ref].append(char)


build_stacks(drawing)


# Build function for moving a crate from one stack to another
def execute_instruction(instrutionc, crane_type):
	_, quant, __, origin, ___, destination = instruction.split(" ")
	quant = int(quant)
	origin = int(origin) -1
	destination = int(destination) -1
	crate = -quant - 1

	if crane_type == 9000:
		stacks[destination] += (stacks[origin][:crate:-1])
		del stacks[origin][:crate:-1]
	elif crane_type == 9001:
		stacks[destination] += (stacks[origin][crate+1:])
		del stacks[origin][:crate:-1]


for instruction in instructions:
	execute_instruction(instruction, crane_type)


# print the top crate of each stack
def tops():
	print("".join([stack[-1] for stack in stacks]))

tops()
