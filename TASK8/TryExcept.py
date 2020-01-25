n = int(input("Enter a number : "))
l = [0,1,2,3,4,5,6,7,8,9,10]
for i in l:
	try:
		print(n/i)
	except ZeroDivisionError:
		print("Invalid Calculation")	