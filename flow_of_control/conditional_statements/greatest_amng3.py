num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
num3=int(input("enter third number : "))
if num1>num2 and num1>num3:
    print("greatst is ",num1)
elif num2>num1 and num2>num3:
    print("greatest is ",num2)
#elif num1==num2 or num1==num3 or num2==num3:
elif num1==num2==num3:
    print("all are equal")
else:
    print("greatest is ",num3)