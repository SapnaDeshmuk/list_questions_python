elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
sum_even=0
sum_odd=0
i=0
count_even=0
count_odd=0
while i<len(elements):
	if elements[i]%2==0:
		sum_even=sum_even+elements[i]
		count_even=count_even+1
		average_even=sum_even/count_even
	else:
		sum_odd=sum_odd+elements[i]
		count_odd=count_odd+1
		average_odd=sum_odd/count_odd
	i=i+1
count_oddeven=count_even+count_odd
sum_oddeven=sum_even+sum_odd
average_oddeven=average_even+average_odd
print count_odd
print count_even
print count_oddeven
print sum_even
print sum_odd
print sum_oddeven
print average_even
print average_odd
print average_oddeven
