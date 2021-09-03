def square(num):
    k=num
    for i in range(num):
        for j in range(num):
            print("*",end=" ")
        print()
num=int(input("enter the range : "))
square(num)