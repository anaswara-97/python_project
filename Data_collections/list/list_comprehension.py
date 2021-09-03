# a=[3,2,4,5,6,7]
# print(a)
# b=[]
# mul=0
# for i in a:
#     mul=i*5
#     b.append(mul)
# print(b)

#number of lines can be reduced using comprehension
#in list comprehension code is written inside
# the list brackets and seperate using whitespaces
#inside the bracket, first the element or operation is s
#eg

n=[3,2,4,5,6,7]
b=[i*5 for i in n]
print(b)