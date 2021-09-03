def fact(num):
    if num==1:
        return 1
    elif num==0:
        return 1
    else:
        return num*fact(num-1)

print("factorial of 5 : ",fact(5))