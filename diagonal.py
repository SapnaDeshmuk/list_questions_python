magic_square=[[1,2,3],[1,2,3],[1,2,3]]
i=0
new_list=[]
j=0
sum=0
while i<len(magic_square):
	new_list.append(magic_square[i][j])
	sum=sum+new_list[i]
	j=j+1
	i=i+1
print new_list
magic_square=[[1,2,3],[1,2,3],[1,2,3]]
i=0
new_list=[]
j=2
sum1=0
while i<len(magic_square):
	new_list.append(magic_square[i][j])
	sum1=sum1+new_list[i]
	j=j-1
	i=i+1
print new_list
print sum+sum1
    