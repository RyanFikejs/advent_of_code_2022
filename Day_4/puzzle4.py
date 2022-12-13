"""Day 4, puzzle 1 of the Advent of Code 2022"""

with open("input.txt", "r") as f:
	cleaning_assignments = [line for line in f]
f.close()

for ind, assignment in enumerate(cleaning_assignments):
	cleaning_assignments[ind] = assignment.split(",")
	cleaning_assignments[ind][1] = cleaning_assignments[ind][1].split("\n")[0]

def check_contains(
		start_a,
		end_a,
		start_b,
		end_b
	):

		# print(f"A: {start_a} to {end_a}\nB: {start_b} to {end_b}")
		if start_a <= start_b:
			if end_b <= end_a:
				return 1

		return 0

def check_any_overlap(
		start_a,
		end_a,
		start_b,
		end_b
	):
	
		if start_b >= start_a:
			if start_b <= end_a:
				return 1

		if end_b >= start_a:
			if end_b <=end_a:
				return 1

		return 0
		
contains_count = 0
any_overlap = 0

for assignment in cleaning_assignments:
	range_0 = abs(eval(assignment[0]))
	range_1 = abs(eval(assignment[1]))
	start_0, end_0 = assignment[0].split("-")
	start_0 = int(start_0)
	end_0 = int(end_0)
	start_1, end_1 = assignment[1].split("-")
	start_1 = int(start_1)
	end_1 = int(end_1)

	if range_0 > range_1:
		contains_count += check_contains(
			start_0,
			end_0,
			start_1,
			end_1
		)
		any_overlap += check_any_overlap(
			start_0,
			end_0,
			start_1,
			end_1
		)

	elif range_1 > range_0:
		contains_count += check_contains(
			start_1,
			end_1,
			start_0,
			end_0
		)
		any_overlap += check_any_overlap(
			start_1,
			end_1,
			start_0,
			end_0
		)

	else:
		if start_0 == start_1:
			contains_count += 1
		any_overlap += check_any_overlap(
			start_0,
			end_0,
			start_1,
			end_1
		)

print(f"{contains_count} overlapping pairs with one assignment completely contained.")
print(f"{any_overlap} overlapping pairs in all.")