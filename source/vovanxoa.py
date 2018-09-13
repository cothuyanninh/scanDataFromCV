import requests, bs4
filetxtreading = open('C:\\Users\\vanquangcz\\Desktop\\python\\project\\data\\temp\\linkCV.txt', 'r').readlines()

def scanFromTXT():
	print((filetxtreading))
	for i in range(len(filetxtreading)):
		res = requests.get(filetxtreading[i])
		print(res)


scanFromTXT()