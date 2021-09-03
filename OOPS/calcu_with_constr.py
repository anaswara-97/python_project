class Calculator:
    def __init__(self,num1,num2,cho):
        self.num1 = num1
        self.num2 = num2
        self.cho=cho
        if self.cho==1:
            print("Result = ",self.num1 + self.num2,"\n------------------------")
        elif self.cho==2:
            print("Result = ",self.num1 - self.num2,"\n------------------------")
        elif self.cho==3:
            print("Result = ",self.num1 * self.num2,"\n------------------------")
        elif self.cho==4:
            print("Result = ",self.num1 / self.num2,"\n------------------------")
        elif self.cho == 5:
            exit(0)
n=0
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
while n!=1:
    print("1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
    cho=int(input("enter your choice : "))
    c=Calculator(num1,num2,cho)