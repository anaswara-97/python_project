def pyramid(num):
    for i in range(num):
        k = num
        for k in range(num):
            print(end=" ")
        num=num-1
        for j in range(0,i+1):
            print("*",end=" ")
        print()
num=int(input("enter  the range : "))
pyramid(num)