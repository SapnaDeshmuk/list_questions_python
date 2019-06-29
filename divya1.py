list_number=[2,5,8,7,9,6]
a=[8,7]
b=[2,9]
c=[2,6]
d=[7,9,6]
i=0
while i<=len(list_number):
    if list_number [i]==8 and list[i+1]==7:
        print"yes"
    else:
        print "false"
    elif list_number[i]==2 and list_number[i+1]==9:
        print "true"
    else:
        print "false"
    elif list_number[i]==2 and list_number[i+1]==6:
        print"true"
    else:
        print"false"
    elif list_number[i]==7 and list_number[i+1]==9 and list_number[i+2]==6:
        print "true"
    else:
        print "false"
    i=i+1