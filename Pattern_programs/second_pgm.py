num=int(input("enter range : "))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()