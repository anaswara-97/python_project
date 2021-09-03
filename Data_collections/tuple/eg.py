t1=(2,4,3,"hello",5)
print(t1)
print(type(t1))
t1=2,4,3,5,(5,7)
print(t1)

t2=2,6,7,8,
print(t2)
print("minimum value: ",min(t2))
print("maximum value: ",max(t2))
print("total length: ",len(t2))

print(t2[0])
print(t2[-1])
print(t2[1:3])

#tuple with on element
t=2,    #t=2
print(type(t))

#tuple unpacking
t4=2,4,'hai',5
a,b,c,d=t4
print(a)
print(b)
print(c)
print(d)
