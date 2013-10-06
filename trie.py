
_end = '_end_'
root = dict()

def make_trie(words):
	for word in words:
		current_dict = root
		for parse in word:
			for letter in parse:
				current_dict = current_dict.setdefault(letter, {})
		current_dict = current_dict.setdefault(_end, word)
	return root

def findInTrie(word):
	found = True;
	current_dict = root
	for parse in word:
		for letter in parse:
			if letter not in current_dict:
				print letter
				found = False
			else:
				current_dict = current_dict.setdefault(letter, {})
	current_dict = current_dict.setdefault(_end, word)
	return found

def findInTrie(allowedMiss, current_dict, word, index, MissedChar):

	
	if MissedChar == (allowedMiss+1):
		return 0
	if index == len(word) and _end in current_dict and MissedChar == allowedMiss:
		print "----> %s" % current_dict[_end]
		return 1
	if index == len(word):
		return 0;
	
	for key in current_dict:
		if word[index] == key:
			childDict = current_dict.setdefault(key, {})
			findInTrie(allowedMiss, childDict, word, index+1, MissedChar);
		else:
			childDict = current_dict.setdefault(key, {})
			findInTrie(allowedMiss, childDict, word, index+1, MissedChar+1);

from sys import argv
script, inputDict = argv
inputFile = open(inputDict)
dictData = inputFile.read()	
make_trie(dictData.split(" "))
findInTrie( 3, root, "fot", 0, 0);