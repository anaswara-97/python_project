class A:
    def printA(self):
        print("parent class A")
class B(A):
    def printB(self):
        print("child class A")
        print("parent class of C")
class C(B):
    def printC(self):
        print("child class of B")
a=A()
a.printA()
print("--------------")
b=B()
b.printB()
b.printA()
print("--------------")
c=C()
c.printC()
c.printB()
c.printA()