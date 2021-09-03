# a=int(input("enter the range : "))
# b=set()
# for i in range(a):
#     c=int(input("enter the element : "))
#     c*=c
#     b.add(c)
# print(b)

a={2,4,2,7,6}
b=set()
for i in a:
    b.add(i**2)
print(a)
print("squares of first set...")
print(b)