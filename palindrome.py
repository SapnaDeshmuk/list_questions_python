name=[ 'n', 'i', 't', 'i', 'n' ]
a=0
b=-1
while a<len(name):
	if name[a]==name[b]:
		var="ha!palindrome hai"
	else:
		var="nhi!palindrome nhi hai"
	a=a+1
	b=b-1
print var
