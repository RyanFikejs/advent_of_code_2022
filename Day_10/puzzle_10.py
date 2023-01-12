"""Solutions for puzzle 10 of Advent of Code 2022"""

with open("input.txt", "r") as f:
	try:
		cpu_instructions = [line.strip("\n") for line in f]
	finally:
		f.close()

cycle = 1
x_register = 1
signal_strengths = []
image_map = []

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

		draw_pixel()
		cycle += 1
		# draw_pixel()

		# if calculate_signal:
		# 	calculate_signal_strength()
	else:
		_, amount = cpu_instruction.split(" ")
		amount = int(amount)

		if calculate_signal:
			calculate_signal_strength()
			calculate_signal = False

		draw_pixel()
		cycle += 1
		# draw_pixel()

		if signal_strength_relay:
			if cycle % 40 == 20:
				calculate_signal_strength()

		draw_pixel()
		cycle += 1
		# draw_pixel()
		x_register += amount
		# draw_pixel()

def draw_pixel(sprite=False):
	global cycle
	global x_register
	global image_map

	drawing_pixel = cycle % 40 - 1
	L = x_register -1
	R = x_register + 2

	if drawing_pixel in range(L, R):
		sprite = True

	if sprite:
		pixel = "#"
	else:
		pixel = "."

	image_map.append(pixel)

def render_image():
	global image_map

	image_lines = [
		''.join(image_map[n:n+40]) for n in range(0,len(image_map), 40)
	]

	for line in image_lines:
		print(line)


if __name__ == "__main__":
	for i in cpu_instructions:
		read_instruction(i, signal_strength_relay=True)

	# print(signal_strengths)
	print(f"Sum of {len(signal_strengths)} signal strengths: {sum(signal_strengths)}")
	render_image()

