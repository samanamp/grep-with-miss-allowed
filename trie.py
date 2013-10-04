
_end = '_end_'
root = dict()

def make_trie(words):
	for word in words:
		current_dict = root
		for parse in word:
			for letter in parse:
				current_dict = current_dict.setdefault(letter, {})
		current_dict = current_dict.setdefault(_end, _end)
	return root


from sys import argv
script, inputDict = argv
inputFile = open(inputDict)
dictData = inputFile.read()	
print make_trie(dictData.split(" "))