kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count_crorepati=0
count_lakhpati=0
count_dilwale=0
while i<len(kitna_paisa_hai): 
	if kitna_paisa_hai[i] >=10000000:
		count_crorepati=count_crorepati+1
	elif kitna_paisa_hai[i]>100000 and kitna_paisa_hai[i] <10000000:
		count_lakhpati=count_lakhpati+1
	else: 
		count_dilwale=count_dilwale+1
	i=i+1
print count_crorepati,"crorepati hai"
print count_lakhpati,"lakhpati hai"
print count_dilwale,"dilwale hai"


