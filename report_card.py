marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
new_list=[]
sum=0
while i<len(marks):
	j=0
	while j<len(marks[i]):
		sum=sum+marks[i][j]
		j=j+1
	i=i+1
new_list.append(sum)
print new_list
