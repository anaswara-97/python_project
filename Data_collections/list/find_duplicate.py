a=[2,3,4,5,6,3,6,7,8,9]
print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)