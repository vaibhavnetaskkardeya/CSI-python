def maxlength():
	n = int(input("enter no. of elements : "))
	i=0
	max = 0
	name = []
	for i in range(0,n):
			s = str(input())
			name.append(s)
			if max<len(s):
				max = len(s)
			i = i+1
	print(max)		


maxlength()

