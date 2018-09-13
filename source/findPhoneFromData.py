import re

def findNumberPhone(data):
	phoneNumRegex10number = re.compile(r'\s\d\d\d\d\d\d\d\d\d\d\s')
	phoneNumRegex11number = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\s')
	mo1 = phoneNumRegex10number.findall(data)
	mo2 = phoneNumRegex11number.findall(data)
	if len(mo1) != 0 :
		print(mo1[0])
	if len(mo2) != 0 :
		print(mo2[0])
	if len(mo1) == 0 and len(mo2) == 0:
		print('Exception numberphone')