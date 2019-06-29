list_number=[2,5,8,7,9,6]
a=[5,8,9]
i=0
j=0
res="false"
while i<len(list_number)-1 and j<len(a)-1:
    if list_number [i]==a[j]:
        if list_number[i+1]==a[j+1]:
            res="true"
        else:
            res="false"
        j=j+1
    i=i+1
print res
    #if b in list_number:
       # print "true"
    #else:
        #print "false"
    #if c in list_number:
    #else:
       ## print"false"
    #if d in list_number:
       # print "true"
    #else:
      ##i=i+1