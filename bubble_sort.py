list_number=[11,15,14,12,17,20,16]
i=0
while i<len(list_number):
	j=0
	while j<len(list_number):
		if list_number[i]<list_number[j]:
			next=list_number[i]
			list_number[i]=list_number[j]
			list_number[j]=next
		j=j+1
	i=i+1
print (list_number)

