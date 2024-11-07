"""
File: boggle.py
Name: Christina
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	You will find the anagrams of the letter.
	"""
	# letters = [['f', 'y', 'c', 'l'], ['i', 'o', 'm', 'g'], ['o', 'r', 'i', 'l'], ['h', 'j', 'h', 'u']]
	# use list to simulate matrix
	letters = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
	for i in range(4):
		letter = input(f"{i+1} row of letters: ")
		if legal_check(letter):
			tmp = 0
			for ch in letter:
				if not ch.isspace():
					letters[i][tmp] = ch.lower()
					tmp += 1
		else:
			print("Illegal input")
			break
	start = time.time()
	####################
	dic = read_dictionary()
	used = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # check if ch has been used
	all_find = []  # store the all boggles founded
	for i in range(4):
		for j in range(4):
			cur_str = ""
			find_boggles(letters, cur_str, dic, used, i, j, all_find)
	print(f"There are {len(all_find)} words in total.")
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def legal_check(letter):
	"""
	This function will check if letter is legal.
	"""
	tmp = 0
	for ele in letter:
		if tmp % 2 == 0:
			if not ele.isalpha():
				return False
		else:
			if not ele.isspace():
				return False
		tmp += 1
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return: (dic)
	"""
	dic = {}
	with open(FILE, 'r') as f:
		for line in f:
			if line[0] not in dic:
				dic[line[0]] = []
			if len(line) >= 4:
				dic[line[0]].append(line.strip())
	return dic


def find_boggles(letters, cur_str, dic, used, x, y, all_find):
	"""
	:param letters: (dic)
	:param cur_str: (str)
	:param dic: (dic)
	:param used: (dic)
	:param x: (int)
	:param y: (int)
	:param all_find: (list)
	"""
	cur_str += letters[x][y]
	used[x][y] = 1
	if has_prefix(cur_str, dic):
		if len(cur_str) >= 4:
			# find if cur_str is in dic
			if cur_str in dic[cur_str[0]] and cur_str not in all_find:
				print(f"Found: {cur_str}")
				all_find.append(cur_str)
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x + i < 4 and 0 <= y + j < 4:  # check whether coordinates are out of scope
					if x != x + i or y != y + j:  # check whether x+i, y+j is the same as cur_str[-1]
						if not used[x+i][y+j]:
							find_boggles(letters, cur_str, dic, used, x+i, y+j, all_find)
	used[x][y] = 0
	cur_str = cur_str[:-1]


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic: (dic)
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dic[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
