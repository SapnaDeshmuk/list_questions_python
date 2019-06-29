list_1=[[2,1,2,3,3],[4,5,6],[5,7,8]]
i=0
new_list=[]
while i<len(list_1):
	j=0
	sum=0
	while j<len(list_1[i]):
		sum=sum+list_1[i][j]
		j=j+1
	new_list.append(sum)
	i=i+1
print new_list



