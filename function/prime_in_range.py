low=int(input("Enter the lower limit : "))
high=int(input("Enter the higher limit : "))
if(low>1 and high>1):
    for i in range(low,high+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)
else:
    print("i is not a prime...enter values greater than 1")