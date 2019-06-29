elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count_odd=0
count_even=0
i=0
while i<len(elements):
	if elements[i]%2==0:
		count_even=count_even+1
	else:
		count_odd= count_odd+1
	i=i+1
print ("number of even numbers:",count_even)
print ("number of odd numbers:",count_odd)
		

