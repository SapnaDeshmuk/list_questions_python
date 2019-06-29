magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
new_list=[]
while i<len(magic_square):
	j=0
	sum=0
	while j<len(magic_square[i]):
		sum=sum+magic_square[i][j]
		j=j+1
	new_list.append(sum)
	i=i+1
print new_list
