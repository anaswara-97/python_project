num=int(input("Enter the number : "))
flag=0
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            break
    else:
        flag=1
    if(flag==1):
        print("prime")
    else:
        print("not prime")