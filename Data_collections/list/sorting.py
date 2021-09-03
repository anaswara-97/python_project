a=[-2,3,1,8,7,-6,0,-11,56,30,-29]
print(a)
b=[]
while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    b.append(min)
    a.remove(min)
print("sorted list : \n",b)
