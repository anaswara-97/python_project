num=int(input("enter the range : "))
if(num==0):
    print("0! is 1")
elif(num<0):
    print("no factorial for negative number...enter a positive value")
else:
    prod=1
    for i in range(1,num+1):
        prod*=i
    print("factorial(product) of",num,":",prod)

# using while

# i=1
# while(i<num+1):
#     prod*=i
#     i+=1
# print("factorial(product) of",num,":",prod)