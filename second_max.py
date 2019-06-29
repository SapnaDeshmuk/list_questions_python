list=[19,2,20,25,60,45,4,3,5]
max_num=0
i=0
second_max_num=0
while(i<len(list)):
    if list[i]>max_num:
        max_num=list[i]
    i=i+1
# print max_num 
i=0
while(i<len(list)):
    if list[i]>second_max_num: 
        if list[i]<max_num:
            second_max_num=list[i]
    i=i+1
print second_max_num