import sys
LINE_LIMIT = 70


def processLine(fileLine):
	if len(fileLine) > 0 and fileLine[-1] == "\n":
		fileLine = fileLine[:-1]
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

def main():
	with open(sys.argv[1], "r") as txt: 
		for fileLine in txt:
			processLine(fileLine)

main()