a=int(input("enter num1 : "))
b=int(input("enter num2 : "))
try:
   print("result = ",a/b)
except Exception as e:
    print(e.args)
