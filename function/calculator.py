def add(num1,num2):
    print("Addition result = ",num1+num2)
def sub(num1,num2):
    print("subtraction result = ", num1 - num2)
def mul(num1,num2):
    print("Multiplication result = ", num1 * num2)
def div(num1,num2):
    print("Division result = ", num1 / num2)
def display():
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
    ch=int(input("Select your choice : "))
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    if(ch==1):
        add(num1,num2)
    elif(ch==2):
        sub(num1,num2)
    elif(ch==3):
        mul(num1,num2)
    elif(ch==4):
        div(num1,num2)
    else:
        print("wrong choice!")
    c=input("Do you want to continue(y/n) : ")
    if(c=='y'):
        display()
display()