def pattern(num):
    for i in range(0,num+1):
        for j in range(1,i):
            print(i,end=" ")
            i+=1
        print()
num=int(input("enter the range : "))
pattern(num)