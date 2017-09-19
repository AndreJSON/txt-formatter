import sys
import math
LINE_LIMIT = 70
DIVIDER = "*"


def expandDivider(fileLine):
	line = fileLine[1:]
	if len(line) > 0:
		line = " " + line + " "
	numStars = (LINE_LIMIT - len(line)) / 2
	line = (DIVIDER * math.floor(numStars)) + line + (DIVIDER * math.ceil(numStars))
	print(line)

def splitLine(fileLine):
	while True:
		line = fileLine[:LINE_LIMIT]
		if len(line) < LINE_LIMIT:
			cutOff = LINE_LIMIT
		else:
			cutOff = line.rfind(" ")
			if cutOff == -1:
				cutOff = LINE_LIMIT
		print(fileLine[:cutOff])
		fileLine = fileLine[cutOff:]
		if len(fileLine) == 0:
			break
		elif fileLine[0] == " ":
			fileLine = fileLine[1:]

def processLine(fileLine):
	if fileLine[-1] == "\n":
		fileLine = fileLine[:-1]
	if len(fileLine) > 0 and fileLine[0] == DIVIDER:
		expandDivider(fileLine)
	else:
		splitLine(fileLine)

def main():
	with open(sys.argv[1], "r") as txt: 
		for fileLine in txt:
			processLine(fileLine)

main()