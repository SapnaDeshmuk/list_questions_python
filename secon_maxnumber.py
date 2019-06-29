numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7,100]
max=1
i=0
while i<len(numbers):
	if max<numbers[i]:
		max=numbers[i]
	i=i+1
second_max=0
a=0
while a<len(numbers):
	if max>numbers[a]and second_max <numbers[a]:
		second_max=numbers[a]
	a=a+1
print second_max
