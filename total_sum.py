number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
j=i+1
sum=30
while i<len(n):
	while j <len(n):
		if n[i]+n[j]==sum:
			print n[i]+n[j]
			i=i+1
			j=j+1
		