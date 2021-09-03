a=[2,4,1,5,7,6]
print(a)
b=[i for i in a if i%2==0]
c=[i for i in a if i%2!=0]
print("even numbers in the list : ",b)
print("odd numbers in the list : ",c)