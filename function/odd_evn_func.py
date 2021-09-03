def oddOrEven():
    num=int(input("enter the number : "))
    if(num<0):
        print(num," is a negative number..please enter positive number")
    else:
        if(num%2==0):
            print(num," is even")
        else:
            print(num," is odd")
oddOrEven()