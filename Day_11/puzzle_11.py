"""Solutions for puzzle 11 of Advent of Code 2022"""

import math

with open("input.txt", "r") as f:
	try:
		monkey_observations = [line.strip("\n").lstrip() for line in f if line != "\n"]
	finally:
		f.close()

# monkey_crew =

def sort_monkey_stats(observations):
	monkey_list = []
	monkey = None

	for i,line in enumerate(observations):
		ii = i % 6

		if ii == 0:
			monkey = Monkey()
			monkey.name = line.split(":")[0]
		elif ii == 1:
			monkey.item_queue = [
				int(item) for item in line.split(":")[1].lstrip().split(",")
			]
		elif ii == 2:
			monkey.operation = line.split("=")[-1].lstrip()
		elif ii == 3:
			monkey.test_criteria = int(line.split(" ")[-1])
		elif ii == 4:
			monkey.next_true = int(line.split(" ")[-1].lstrip())
		else:
			monkey.next_false = int(line.split(" ")[-1].lstrip())
			monkey_list.append(monkey)
			monkey = None

	return monkey_list

class Monkey:
	def __init__(self):
		self.name = ""
		self.item_queue = []
		self.inspected_items = 0
		self.operation = ""
		self.test_criteria = None
		self.next_true = None
		self.next_false = None

	def assess_item(self, item):
		if item % self.test_criteria == 0:
			return self.next_true
		else:
			return self.next_false

	def inspect_item(self, relief=True):
		self.inspected_items += 1
		old = self.item_queue.pop(0)
		new = eval(self.operation)
		
		if relief:
			new //= 3

		return new

	def intense_inspection(self):
		self.inspected_items += 1
		old = self.item_queue.pop(0)
		new = eval(self.operation)

		return new

def toss_around(monkeys, rounds, relief=True):
	for t in range(rounds):
		for monkey in monkeys:
			while monkey.item_queue != []:
				# item =monkey.inspect_item(relief=relief)
				if relief:
					item = monkey.inspect_item()
				else:
					item = monkey.intense_inspection()
				which_monkey = monkey.assess_item(item)
				monkey_crew[which_monkey].item_queue.append(item)

def caluculate_monkey_business(monkeys):
	inspection_rankings = []

	for monkey in monkeys:
		print(f"{monkey.name} inspected {monkey.inspected_items} items.")
		inspection_rankings.append(monkey.inspected_items)
	
	inspection_rankings = sorted(inspection_rankings)
	
	return math.prod(inspection_rankings[-2:])



if __name__ == "__main__":
	#  Calculate 20 rounds with relief
	# monkey_crew = sort_monkey_stats(monkey_observations)
	# rounds = 20

	# toss_around(monkey_crew, rounds)

	# monkey_business = caluculate_monkey_business(monkey_crew)
	# print(f"Monkey business after 20 rounds with relief: {monkey_business}")

	# Calculate 10000 rounds without relief
	monkey_crew = sort_monkey_stats(monkey_observations)
	rounds = 10000
	
	toss_around(monkey_crew, 10000)

	monkey_business = caluculate_monkey_business(monkey_crew)
	print(f"Monkey business after 10,000 rounds without relief: {monkey_business}")


