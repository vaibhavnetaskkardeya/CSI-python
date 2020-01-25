a = int(input("enter fist side : "))
b = int(input("enter second side : "))
c = int(input("enter third side : "))
if a==b==c:
	print("equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")	
else:
	print("scalene triangle")	
	