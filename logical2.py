list_element=[1,10,2,13,15]
i=0
sum=0
new=[]
while i<=len(list_element):
    j=i+1
    while j<len(list_element):
        sum=list_element[i]+list_element[j]
        if sum==12:
            new.append([list_element[i],list_element[j]])
        j=j+1
    i=i+1
print new