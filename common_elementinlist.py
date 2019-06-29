list1=[1,2,3,4,5,6]
list2=[2,3,4,5,11,15]
list3=[]
i=0
while i<len(list1):
	if list1[i] in list2:
		list3.append(list1[i])
	i=i+1
print list3
