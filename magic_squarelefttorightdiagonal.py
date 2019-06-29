magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
new_list=[]
j=0
sum=0
while i<len(magic_square):
	new_list.append(magic_square[i][j])
	sum=sum+new_list[i]
	j=j+1
	i=i+1
print sum
print new_list
    