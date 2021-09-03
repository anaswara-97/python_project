def factorial(num):
    if(num==0):
        print(num,"! is 1")
    elif(num<0):
        print(num,"is a negative number,there is no factorial for negative number")
    else:
        fact=1
        for i in range(fact,num+1):
            fact*=i
        print("factorial of ",num," is ",fact)
factorial(8)
factorial(-6)
factorial(0)