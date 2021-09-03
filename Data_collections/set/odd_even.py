a={1,2,3,4,5,6,7,8,9}
print("primary set : ",a)
odd=set()
even=set()
for i in a:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print("odd number set : ",odd)
print("even number set : ",even)