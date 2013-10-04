#File Transformer
#Knowledge Technology Subject
#Saman Abdolmohammadpour (591703)
from sys import argv
script, input, output = argv
inputFile = open(input)
outputFile = open(output, 'w')
lastOneScape = False
while True:
	inputData = inputFile.read(1)
	if not inputData:
		print "Finished Transforming! HoOrRay my first Python Program :-)"
		break
	if inputData.isalpha() or inputData == " ":
		if lastOneScape and inputData == " ":
			continue
		else:
			outputFile.write(inputData.lower())
			if inputData == " ":
				lastOneScape = True;
			else:
				lastOneScape = False;