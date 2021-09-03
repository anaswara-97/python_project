lst=[3,5,7] #[10,8,6]
tot=sum(lst)
# lst2=[tot-i for i in lst]
# print(lst2)

# or

print(list(map(lambda num:tot-num,lst)))

# tot=0
# for i in lst:
#     tot=sum(lst)-i
#     lst2.append(tot)
# print(lst2)



print("------------------------------")

sum=[2,3,4,5] #
# total=7
# for i in sum:
#     for j in sum:
#         if i!=j:
#             if total==i+j:
#                 print("(",i,",",j,")")

# # OR
#
# total=9
# for i in range(len(sum)):
#     for j in range(i+1,len(sum)):
#         if sum[i]+sum[j]==total:
#             print("(",sum[i],",",sum[j],")")

# OR

low=0
upp=len(sum)-1
total=7
my_lst=[]
while(low<upp):  #o(n) complexity because no nested loops
    sum1=sum[low]+sum[upp]
    if sum1==total:
        my_lst.append((sum[low],sum[upp]))
        low = low + 1
    elif(sum1>total):
        upp=upp-1
    elif(sum1<total):
        low=low+1
print(my_lst)