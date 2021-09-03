lst_1=[10,11,12,20,21,30]
lst_2=[20,21,22,23,24,30]

# find common elements withount using builtin functions
cnt=0
for i in lst_1:
    if i in lst_2:
        print(i,end=",")
