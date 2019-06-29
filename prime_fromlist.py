numbers=[3,4,5,6,7,8,9,11,12,13,15,16,17]
i=0
while i<len(numbers):
	j=2
	while j<numbers[i]:
		if numbers[i]%j==0:
			print"not prime",numbers[i]
			break
		j=j+1
	else:
		print"prime",numbers[i]
	i=i+1
