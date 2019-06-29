elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
new=[]
new1=0
while i<len(elements):
	if elements [i]%2==0:
		new.append(list[i])
		sum=sum+list[i]
		sum_even=sum
		i=i+1
	else:
		new1.append(list[i])
		sum=sum+list[i]
		sum_odd=sum
		i=i+i
print sum_even
print sum_odd


