a=int(input("enter num1 : "))
b=int(input("enter num2 : "))
if b>a:
    raise Exception("second number is greater")
else:
    print(a/b)