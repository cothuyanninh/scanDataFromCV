import docx, re
from findPhoneFromData import findNumberPhone
from findEmailFromData import findEmail
from findNameFromData import findName
from getDataFromWord import get_docx_text

def scanFromWORD(linkFile):
	result = open('result', 'w')
	print('Ten: ', end =' ')
	findName(get_docx_text(linkFile).split('\n'))
	print('\n')
	print('SDT: ', end = ' ')
	findNumberPhone(get_docx_text(linkFile))
	print('\n')
	print('Email: ', end = ' ')
	findEmail(get_docx_text(linkFile))
	print('\n')