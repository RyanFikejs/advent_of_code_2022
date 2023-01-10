"""Puzzles for Day 13 of the Advent of Code 2022"""

import sys

with open("input.txt", 'r') as f:
	try:
		packets = [line.strip("\n").lstrip() for line in f]
		packet_pairs = [[eval(packets[n]), eval(packets[n+1])] for n in range(0,len(packets),3)]
	finally:
		f.close()
print(packet_pairs[-1])


def compare_lists(list_1, list_2):
	"""
	Compares the items in two lists (assuming that the list contains integers and
	arrays only), index by index. If the item at a given index is a list/array 
	while the other is an integer, the integer is made a the sole item of a new
	list for comparison.
	"""

	def compare_items(item_1, item_2):
		if isinstance(item_1, int) & isinstance(item_2, int):
			return item_1 <= item_2
		elif isinstance(item_1, list) & isinstance(item_2, list):
			

	current_1 = list_1[0]
	current_2 = list_2[0]

	while current_1:
		if current_1