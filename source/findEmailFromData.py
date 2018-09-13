import re

def findEmail(data):
	matches =[]
	emailRegex = re.compile('''(
	[a-zA-z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

	for groups in emailRegex.findall(data):
		matches.append(groups[0])
	if (len(matches) != 0):
		print(matches[0])
	else :
		print("Exception email")


