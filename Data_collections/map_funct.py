lst=[2,3,1,5,6]
lst1=[]
# squares of all numbers
for num in lst:
    c=num**2
    lst1.append(c)
print(lst1)
print("-------------")
# square=list(map(square,lst))
# print(square)

from functools import reduce

lst2=[2,3,1,5,6]

total=reduce(lambda num1,num2:num1+num2,lst2)
print("sum :",total)

cubes=list(map(lambda num:num**3,lst2))
print(cubes)

squares=list(map(lambda num:num**2,lst2))
print(squares)

print("-------------")

def square(num):
    return num**2
square=list(map(square,lst2))
print(square)

print("-------------")

def cube(num):
    return num**3
cubes=list(map(cube,lst2))
print(cubes)

print("-------------")

num1=10
num2=45
print("largest : ",num1 if num1>num2 else num2)

num1=-19
print("negative : ",num1 if num1<0 else num2,"\npositive : ",num1 if num1>0 else num2)
