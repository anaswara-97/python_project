def parallellogram(num):
    for i in range(num):
        k=num
        for k in range(i):
            print(end=" ")
        k=k+1
        for j in range(num):
            print("*",end=" ")
        print()
num=int(input("enter the range : "))
parallellogram(num)