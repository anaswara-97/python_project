num=int(input("enter the limit : "))
sum=0
# for i in range(num+1):
#     sum=sum+i
# print("sum of first",num,"numbers :",sum)

i=0
while(i<=num):
    sum+=i
    i+=1
print("sum of first",num,"numbers :",sum)
