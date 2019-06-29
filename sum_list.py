list_1=[[8,5,9,],[7,9,10],[12,18,9]]
i=0	
sum1=0
new = []
while i<len(list_1):
	j=0
	while j<len(list_1):
		sum1=sum1+list_1[i][j]
		j=j+1
	new.append(sum1)
	sum1=0
	i=i+1
print new
	