class Add:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("result = ",self.num1+self.num2)
a=Add()
num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))
a.add(num1,num2)
