mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
new=mainStr.split()
print new
substr="over"
replacementStr="on"
i=0
while i<len(new):
	if new[i]==substr:
		new[i]=replacementStr
	i=i+1
a=" ".join(new)
print a