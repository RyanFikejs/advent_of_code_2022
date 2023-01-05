"""Puzzles for Day 7 of the Advent of Code 2022"""

import sys

with open("input.txt", 'r') as f:
	try:
		CLI_log = [line.strip("\n") for line in f]
	finally:
		f.close()

home_directory = None
current_directory = None


## create file objects which are also graph nodes

class File:
	def __init__(self, file_name, parent_directory=None, size=None):
		if size:
			file_type = "data_file"
		else:
			file_type = "directory"

		self.parent = parent_directory
		self.children = None
		self.file_type = file_type
		self.size = size
		self.name = file_name
		# print(f"{self.name} created!")

	def get_size(self, update_dir=False, directories_only=False):
		"""
		Method for gathering information on the sizes of files.
		included are options for writing the file and filtering results.
		"""
		update_option = update_dir
		directories_option = directories_only


		if directories_option:
			if self.file_type == "directory":
				if self.size:
					return self.size
				else:
					return file.get_size(update_dir=True)
		else:
			if self.file_type == "data_file":
				return self.size
			else:
				directory_size = sum(
					[file.get_size(update_dir=update_option) for file in self.children.values()]
				)
				if update_dir:
					self.size = directory_size

				return directory_size

	def add_child(self, file):
		if self.children:
			self.children[file.name] = file
		else:
			self.children = {
				file.name: file
			}
		# print(f"{file.name} is now a child of {self.name}")


# function to read CLI log line
def read_log(line):
	global home_directory
	global current_directory
	# print(line)
	line = [part for part in line.split(" ")]

	if line[0] == "$":
		if line[1] == "cd":
			directory = line[2]
			if directory == "..":
				current_directory = current_directory.parent
			elif directory == "/":
				home_directory = File(file_name="home_directory")
				home_directory.file_type = "directory"
				current_directory = home_directory
			else:
				current_directory = current_directory.children[directory]
	elif line[0] == "dir":
		file_name = line[1]
		global_variables = globals()
		global_variables.__setitem__(
			file_name,
			File(
				file_name=file_name,
				parent_directory=current_directory
			)
		)
		current_directory.add_child(global_variables[file_name])
	else:
		file_name = line[1]
		global_variables = globals()
		global_variables[file_name] = File(
			file_name=file_name,
			parent_directory=current_directory,
			size=int(line[0])
			)
		current_directory.add_child(global_variables[file_name])



for line in CLI_log:
	read_log(line)
	# print(f"current directory: {current_directory.name}")


# Map the home directory with values for sub directories
home_directory.get_size(update_dir=True)


## Answer first question
first_question = 0
question_queue = []


def add_subdirectories_to_queue(directory):
	global question_queue

	for file in directory.children.values():
		if file.file_type == "directory":
			# print(f"{file.name} is a child of {file.parent.name} and takes up {file.size}")
			question_queue.append(file)
			add_subdirectories_to_queue(file)
			

add_subdirectories_to_queue(home_directory)

# Then traverse graph to sum up memory used by each directory
while question_queue != []:
	directory = question_queue[0]

	if directory.size <= 100000:
		first_question += directory.size
		if directory.size == 0:
			print("Warning, 'get_size()' method may not have run properly.")
	
	question_queue.pop(0)

print(first_question)


# Calculate the free space currently available
free_space = 70000000 - home_directory.size

# Calculate the difference to be made up for a 30,000,000 file download
space_needed = 30000000 - free_space
print(f"Need {space_needed} free space")

# Add directories to the queue
add_subdirectories_to_queue(home_directory)

# Find and return the size of the smallest driectory which would free up enough space
smallest_over_needed = free_space

while question_queue != []:
	directory = question_queue[0]
	size = directory.size

	if size >= space_needed:
		if size < smallest_over_needed:
			smallest_over_needed = directory.size

	question_queue.pop(0)

print(f"Size of directory to delete: {smallest_over_needed}")
