class A:
    def dis(self,b):
        self.b=b
    def display(self):
        print(self.b)
    def __str__(self):
        return self.b
a=A()
a.dis("hai")
a.display()
print("obj.reference : ",a)