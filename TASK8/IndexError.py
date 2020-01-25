num = list(map(int,input("Enter list : ").split()))
l = len(num)
for i in range(l+1):
	try:
		print(num[i])
	except IndexError:
		print("Invalid index")	