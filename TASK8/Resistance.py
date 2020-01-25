r1 = int(input("Enter Resistance : "))
r2 = int(input("Enter Resistance : "))
r3 = int(input("Enter Resistance : "))
series = r1+r2+r3
print(series)
try:
	parallel = (1/r1 + 1/r2 + 1/r3)
except ZeroDivisionError:
	print("One of the resistance is zero")
else:
	print(parallel)	