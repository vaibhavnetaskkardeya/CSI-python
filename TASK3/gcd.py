a = int(input("enter first no. : "))
b = int(input("enter secon no. : "))
while (b%a):
	c = b%a
	b = a
	a = c
print(a)