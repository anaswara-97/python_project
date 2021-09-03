def add(n1,n2):
   return n1 + n2
def subt(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2
def floor(n1,n2):
    return n1 // n2
def exp(n1,n2):
    return n1 ** n2
def display():
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Floor division\n6.Exponent\n7.exit")
    ch = int(input("enteryour choice :"))
    if ch == 1:
        print("Result =  ",add(n1, n2))
    elif ch == 2:
        print("Result =  ",subt(n1, n2))
    elif ch == 3:
        print("Result =  ",mul(n1, n2))
    elif ch == 4:
        print("Result =  ",div(n1, n2))
    elif ch == 5:
        print("Result =  ",floor(n1, n2))
    elif ch == 6:
        print("Result =  ",exp(n1, n2))
    elif ch==7:
        exit(0)
    else:
        print("Invalid selection!")
n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
display()
ysno=input("do you want to continue (y/n) : ")
while ysno=='y':
    display()


