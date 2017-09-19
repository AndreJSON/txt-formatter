import sys
LINE_LIMIT = 70


def processLine(fileLine):
	while len(fileLine) > 0:
		line = fileLine[:LINE_LIMIT]
		cutOff = line.rfind(" ")
		if cutOff == -1:
			cutOff = LINE_LIMIT
		print(fileLine[:cutOff], end="")
		fileLine = fileLine[cutOff:]

def main():
	with open(sys.argv[1], "r") as txt: 
		for fileLine in txt:
			processLine(fileLine)

main()