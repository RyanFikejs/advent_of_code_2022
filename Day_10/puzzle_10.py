"""Solutions for puzzle 10 of Advent of Code 2022"""

with open("input.txt", "r") as f:
	try:
		cpu_instructions = [line.strip("\n") for line in f]
	finally:
		f.close()

cycle = 1
x_register = 1
signal_strengths = []

def calculate_signal_strength():
	global cycle
	global x_register
	global signal_strengths

	signal_strengths.append(cycle * x_register)

def read_instruction(cpu_instruction, signal_strength_relay=False):
	global cycle
	global x_register
	global signal_strengths
	calculate_signal = False

	if signal_strength_relay:
		if cycle % 40 == 20:
			calculate_signal = True

	if cpu_instruction == "noop":
		if calculate_signal:
			calculate_signal_strength()

		cycle += 1
		# if calculate_signal:
		# 	calculate_signal_strength()
	else:
		_, amount = cpu_instruction.split(" ")
		amount = int(amount)

		if calculate_signal:
			calculate_signal_strength()
			calculate_signal = False

		cycle += 1

		if signal_strength_relay:
			if cycle % 40 == 20:
				calculate_signal_strength()

		cycle += 1
		x_register += amount

		# if calculate_signal:
		# 	calculate_signal_strength()


if __name__ == "__main__":
	for i in cpu_instructions:
		read_instruction(i, signal_strength_relay=True)

	# print(signal_strengths)
	print(f"Sum of {len(signal_strengths)} signal strengths: {sum(signal_strengths)}")
