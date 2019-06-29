numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7,500]
i=0
max_num=0
while i<len(numbers):
	if numbers[i]>max_num:
		max_num=numbers[i]
	i=i+1
print (max_num)