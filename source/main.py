import docx, os
from scanFromWord import scanFromWORD
from scanFromPdf import scanFromPDF
from scanFromTxt import scanFromTXT
from counterFile import count_file_Txt, count_file_Pdf, count_file_Word

inputFileDir = 'C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\input'
fileInInput = os.listdir(inputFileDir)
print("Co tong so file: %d"%(len(fileInInput)))
for var_i in range(len(fileInInput)):
	print("Quet Cv nguoi thu : %d" %(var_i+1))
	# tim file co duoi docx
	if fileInInput[var_i].endswith('.docx') :
		count_file_Word += 1
		scanFromWORD(inputFileDir +'\\' + fileInInput[var_i])
		
	print('-------------------------------------------')
	# tim file co duoi pdf
	if fileInInput[var_i].endswith('.pdf') :
		scanFromPDF(inputFileDir +'\\' + fileInInput[var_i])
	#	count_file_Pdf += 1

	# tim file co duoi txt trong do co chua cac link file CV moi link mot dong
	if fileInInput[var_i].endswith('.txt') :
	#	inputofdef = inputFileDir + '\\' + fileInInput[var_i]
		print(scanFromTXT(inputFileDir +'\\' + fileInInput[var_i]))
	#	print(inputofdef)
		count_file_Txt += 1



print("Da tim duoc %d file Word"%(count_file_Word))
print("Da tim duoc %d file Pdf"%(count_file_Pdf))
print("Da tim duoc %d file Txt"%(count_file_Txt))
