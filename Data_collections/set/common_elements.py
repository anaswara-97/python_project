s1={1,2,55,4,76,34}
s2={3,5,76,5,55}
print("set 1 : ",s1)
print("set 2 : ",s2)
c=set()
for i in s1:
    # for j in s2:
    #     if i==j:
    if i in s2:
            c.add(i)
print("common elements in set 1 and 2 : ",c)
