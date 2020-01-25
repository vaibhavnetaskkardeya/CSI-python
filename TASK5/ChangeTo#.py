#will change even index to '#' 
num = [1,2,3,4,5,6,7,8,9,10]
i=0
for i in range(0,len(num)):
	if i%2==0:
		num[i]='#'
print(num)		