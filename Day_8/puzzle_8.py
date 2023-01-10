"""Puzzles for Day 8 of the Advent of Code 2022"""


with open("input.txt", "r") as f:
	try:
		tree_map = [line.strip("\n") for line in f]
	finally:
		f.close()


# For finding all trees along the perimeter of the map
def add_perimeter_trees(tree_map):
	return sum([len(tree_map[0]) * 2,((len(tree_map) - 2) * 2)])

# For finding out which trees within the perimeter are visible
def add_interior_trees(treemap, test=False):
	if test:
		height = 5
		width = 5
	else:
		height = len(tree_map)
		width = len(tree_map[0])

	visible_interior_trees = 0

	for i in range(1, height-1):
		for j in range(1, width-1):
			tree = tree_map[i][j]
			left_of_tree = [t for t in tree_map[i][:j]]
			right_of_tree = [t for t in tree_map[i][j+1:]]
			above_tree = [tree_map[n][j] for n in range(i)]
			below_tree = [tree_map[n][j] for n in range(i+1, height)]

			# Check all trees to the left
			if tree <= max(left_of_tree):
				# Check all trees to the right
				if tree <= max(right_of_tree):
					# Check all trees above
					if tree <= max(above_tree):
						# Check all trees below
						if tree <= max(below_tree):
							pass
						else:
							visible_interior_trees += 1
					else:
						visible_interior_trees += 1
				else:
					visible_interior_trees += 1
			else:
				visible_interior_trees += 1

			if test:
				print(f"Left: {left_of_tree}, tree: {tree}, right: {right_of_tree}")

	return visible_interior_trees

# For finding the best scenic score
def find_scenic_score(tree_map):
	height = len(tree_map)
	width = len(tree_map[0])
	best_score = 0

	for i in range(1, height-1):
		for j in range(1, width-1):
			tree = tree_map[i][j]
			left_of_tree = [t for t in tree_map[i][:j]]
			right_of_tree = [t for t in tree_map[i][j+1:]]
			above_tree = [tree_map[n][j] for n in range(i)]
			below_tree = [tree_map[n][j] for n in range(i+1, height)]
			sight_left = 0
			sight_right = 0
			sight_above = 0
			sight_below = 0
			go_left = True
			go_right = True
			go_above = True
			go_below = True

			# Check number of trees each direction until similar or taller height
			while left_of_tree != [] and go_left == True:
				next_left = left_of_tree.pop(-1)
				sight_left += 1

				if next_left >= tree:
					go_left = False

			while right_of_tree != [] and go_right == True:
				next_right = right_of_tree.pop(0)
				sight_right += 1

				if next_right >= tree:
					go_right = False

			while above_tree != [] and go_above == True:
				next_above = above_tree.pop(-1)
				sight_above += 1

				if next_above >= tree:
					go_above = False

			while below_tree != [] and go_below == True:
				next_below = below_tree.pop(0)
				sight_below += 1

				if next_below >= tree:
					go_below = False

			score = sight_left * sight_right * sight_above * sight_below

			if score > best_score:
				best_score = score

	return best_score


if __name__=="__main__":
	# Add together all of the visible trees in the map
	visible_trees = 0

	# Calculate number of trees on the perimeter of the map
	visible_trees += add_perimeter_trees(tree_map)

	# Add the number of visible trees within the perimeter
	visible_trees += add_interior_trees(tree_map, test=False)
	print(f"Number of visible trees from outside: {visible_trees}")

	# Calculate the best scenic score
	highest_scenic_score = find_scenic_score(tree_map)
	print(f"Highest scenic score: {highest_scenic_score}")

	