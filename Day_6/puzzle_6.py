"""Puzzles for day six of the Advent of Code 2022"""

with open("input.txt", "r") as f:
	packet = f.read()
	f.close()

def find_marker(packet, marker_length):
	marker_found = False
	_marker_start = 0
	_first_after_marker = marker_length

	while not marker_found:
		segment = packet[_marker_start:_first_after_marker]
		checker = {}
		repeats = False

		for char in segment:
			if char not in checker:
				checker[char] = 1
			else:
				checker[char] += 1
				repeats = True

		if repeats:
			_marker_start += 1
			_first_after_marker += 1
		else:
			marker_found = True

	return _first_after_marker

print(find_marker(packet, 4))
print(find_marker(packet, 14))