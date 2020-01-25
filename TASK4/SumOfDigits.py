num = int(input("Enter no. : "))
sum = 0
while (num>0):
	r = int(num%10)
	sum = sum+r
	num = num/10
print(sum)	